from core.ports.payslip_port import PayslipPort
from core.domain.payslip import PayslipDTO
from datetime import datetime
import calendar
import uuid

from core.ports.servant_port import ServantPort
from core.ports.attendance_port import AttendancePort

# from infrastructure.adapters.repositories import (
#     servant_repository,
#     attendance_repository,
#     loan_repository,
#     utility_settlement_repository,
# )
from infrastructure.utils.calendar_utils import get_month_name
from infrastructure.utils.cast_utils import safe_float

class PayslipService:
    def __init__(self, 
                 attendance_port: AttendancePort,
                 servant_port: ServantPort):
        self.attendance_repository = attendance_port
        self.servant_repository = servant_port

    def generate_payslip(self, servant_id, month, year):
        servant = self.servant_repository.get_servant_by_id(servant_id)
        servant_name = servant.get("name", "")
        wage = safe_float(servant.get("wage", 0))

        start_date = datetime(year, month, 1)
        end_date = datetime(year + 1, 1, 1) if month == 12 else datetime(year, month + 1, 1)

        attendance_dates = attendance_repository.get_attendance_dates_by_servant(servant_id, start_date, end_date)
        calendar_days = list(calendar.Calendar(firstweekday=0).itermonthdays(year, month))

        # total_earnings = wage * len(attendance_dates)
        # total_unsettled_loan = loan_repository.get_total_unsettled_loan(servant_id)
        # total_unsettled_balance = loan_repository.get_total_unsettled_balance(servant_id)
        # total_deductions = loan_repository.get_total_deductions(servant_id, month, year)
        # net_pay = total_earnings - total_deductions
        # utility_summary = utility_settlement_repository.get_summary(servant_id, month, year)
        return {
        "selected_servant_id": servant_id,
        "servant_name": servant_name,
        "selected_month": month,
        "selected_year": year,
        "attendance_dates": attendance_dates,
        "calendar_days": calendar_days,
        "salary_per_day": wage,
        "total_attendance": len(attendance_dates),
        # "total_earnings": total_earnings,
        # "loan_capital": total_unsettled_loan,
        # "loan_balance": total_unsettled_balance,
        # "total_deductions": total_deductions,
        # "net_pay": net_pay,
        # "utility_summary": utility_summary,
        "month_name": get_month_name(month),
   }