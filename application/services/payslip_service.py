from collections import defaultdict
from core.ports.payslip_port import PayslipPort
from core.domain.payslip import PayslipDTO

from datetime import datetime
import calendar
import uuid

from core.ports.servant_port import ServantPort
from core.ports.attendance_port import AttendancePort
from core.ports.wage_adjustment_port import WageAdjustmentPort
from core.ports.settlement_port import SettlementPort
from core.ports.loan_port import LoanPort
from core.ports.utility_port import UtilityPort
from core.ports.utility_settlement_port import UtilitySettlementPort
# from infrastructure.adapters.repositories import (
#     servant_repository,
#     attendance_repository,
#     loan_repository,
#     utility_settlement_repository,
# )
from infrastructure.utils.calendar_utils import get_month_name
from infrastructure.utils.cast_utils import safe_float

class PayslipService:
    def __init__(self, servant_repository: ServantPort,
                 attendance_repository: AttendancePort,
                 adjustment_repository: WageAdjustmentPort,
                 loan_settlement_repository: SettlementPort,
                 loan_repository: LoanPort,
                 utility_repository: UtilityPort,
                 utility_settlement_repository: UtilitySettlementPort):

        self.servant_repository=servant_repository
        self.attendance_repository=attendance_repository
        self.adjustment_repository=adjustment_repository
        self.loan_settlement_repository=loan_settlement_repository
        self.loan_repository=loan_repository
        self.utility_repository=utility_repository
        self.utility_settlement_repository=utility_settlement_repository

    def generate_payslip(self, servant_id, month, year):
        servant = self.servant_repository.get_servant_by_id(servant_id)
        servant_name = servant.id
        servant_name = servant.name
        wage = safe_float(servant.wage)
        start_date = datetime(year, month, 1)
        end_date = datetime(year + 1, 1, 1) if month == 12 else datetime(year, month + 1, 1)

        attendance_dates = self.attendance_repository.get_attendance_dates_by_servant(servant_id, start_date, end_date)
        calendar_days = list(calendar.Calendar(firstweekday=0).itermonthdays(year, month))

        #wage adjustment calculate
        adjustments = self.adjustment_repository.get_wage_adjustments_by_id(servant_id, start_date, end_date)
        adjustment_total = (sum(safe_float(adj["amount"]) for adj in adjustments))

        total_earnings = safe_float(wage * len(attendance_dates)) + adjustment_total

        # loan settlements
        settlements = self.loan_settlement_repository.get_settlement_by_servant(servant_id, start_date, end_date)
        settlement_total = sum(safe_float(set["settled_amount"]) for set in settlements)

        total_deductions = settlement_total
        loan_summary = self.loan_repository.get_loan_summary_by_servant(servant_id)
        total_unsettled_loan = loan_summary["total_loan_amount"]
        total_unsettled_balance = loan_summary["total_remaining_balance"]
        
        net_pay = total_earnings - total_deductions

        # start utility settlements
        
        # Load all utility types
        utilities = self.utility_repository.get_all_utilities()
        utility_lookup = {u.id: u.name for u in utilities}

        # Get settlements for this servant and date range
        utility_settlements = self.utility_settlement_repository.get_utility_summary_by_servant(
            servant_id, start_date, end_date
        )

        # Directly create a list of settlements with utility name
        utility_summary = [
            {
                "utility_type": utility_lookup.get(s["utility_type_id"], "Unknown"),
                "amount": float(s["amount"]),
                "paid_date": s["paid_date"].strftime("%Y-%m-%d") if hasattr(s["paid_date"], "strftime") else s["paid_date"]
            }
            for s in utility_settlements
        ]

        # end utility settlements


        return {
        "selected_servant_id": servant_id,
        "servant_name": servant_name,
        "selected_month": month,
        "selected_year": year,
        "attendance_dates": attendance_dates,
        "calendar_days": calendar_days,
        "salary_per_day": wage,
        "total_attendance": len(attendance_dates),
        "adjustments": adjustments,
        "total_earnings": total_earnings,
        "settlements":settlements,
        "total_deductions": total_deductions,
        "loan_capital": total_unsettled_loan,
        "loan_balance": total_unsettled_balance,
        "net_pay": net_pay,
        "utility_summary": utility_summary,
        "month_name": get_month_name(month)
   }