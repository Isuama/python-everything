#db
from infrastructure.database.cosmos import CosmosDB
from infrastructure.adapters.container_registry.cosmos_container_registry import CosmosContainerRegistry

# repositories
from infrastructure.adapters.repositories.cosmos.servant_repository import CosmosServantRepository
from infrastructure.adapters.repositories.cosmos.wage_repository import CosmosWageRepository
from infrastructure.adapters.repositories.cosmos.utility_repository import CosmosUtilityRepository
from infrastructure.adapters.repositories.cosmos.utility_settlement_repository import CosmosUtilitySettlementRepository
from infrastructure.adapters.repositories.cosmos.bonus_repository import CosmosBonusRepository
from infrastructure.adapters.repositories.cosmos.loan_repository import CosmosLoanRepository
from infrastructure.adapters.repositories.cosmos.attendance_repository import CosmosAttendanceRepository
from infrastructure.adapters.repositories.cosmos.wage_adjustments_repository import CosmosWageAdjustmentRepository
from infrastructure.adapters.repositories.cosmos.settlement_repository import CosmosSettlementRepository
#from infrastructure.repositories.cosmos.dashboard_repository import DashboardRepository

# services
from application.services.servant_service import ServantService
from application.services.wage_service import WageService
from application.services.utility_service import UtilityService
from application.services.utility_settlement_service import UtilitySettlementService
from application.services.bonus_service import BonusService
from application.services.loan_service import LoanService
from application.services.attendance_service import AttendanceService
from application.services.wage_adjustments_service import WageAdjustmentService
#from application.services.dashboard_service import DashboardService
#from application.services.payslip_service import PayslipService

# Create CosmosDB only once
db_instance = CosmosDB()
registry = CosmosContainerRegistry(db_instance)

def get_servant_service():
    servant_container = registry.get("servants")
    repository = CosmosServantRepository(servant_container)
    return ServantService(repository)

def get_attendance_Service():
    servant_container = registry.get("servants")
    servant_repository = CosmosServantRepository(servant_container)
    attendance_container = registry.get("attendance")
    attendance_repository = CosmosAttendanceRepository(attendance_container)
    return AttendanceService(servant_repository,attendance_repository)

def get_utility_service():
    utility_container = registry.get("utility")
    repository = CosmosUtilityRepository(utility_container)
    return UtilityService(repository)

def get_utility_settlement_service():
    servant_container = registry.get("servants")
    servant_repository = CosmosServantRepository(servant_container)
    utility_container = registry.get("utility")
    utility_repository = CosmosUtilityRepository(utility_container)
    utility_settlement_container = registry.get("utilitySettlement")
    utility_settlement_repository = CosmosUtilitySettlementRepository(utility_settlement_container)
    return UtilitySettlementService(servant_repository,utility_repository,utility_settlement_repository)

def get_bonus_service():
    servant_container = registry.get("servants")
    servant_repository = CosmosServantRepository(servant_container)
    bonus_container = registry.get("bonuses")
    bonus_repository = CosmosBonusRepository(bonus_container)
    return BonusService(servant_repository,bonus_repository)

def get_loan_service():
    servant_container = registry.get("servants")
    servant_repository = CosmosServantRepository(servant_container)
    loan_container = registry.get("loans")
    loan_repository = CosmosLoanRepository(loan_container)
    loan_settlement_container = registry.get("loanSettlements")
    loan_settlement_repository = CosmosSettlementRepository(loan_settlement_container)
    return LoanService(loan_repository,loan_settlement_repository)

def get_wage_service():
    servant_container = registry.get("servants")
    servant_repository = CosmosServantRepository(servant_container)
    wage_container = registry.get("wages")
    wage_repository = CosmosWageRepository(wage_container)
    return WageService(servant_repository,wage_repository)

def get_wage_adjustment_Service():
    servant_container = registry.get("servants")
    servant_repository = CosmosServantRepository(servant_container)
    wage_adjustment_container = registry.get("wageAdjustments")
    wage_adjustment_repository = CosmosWageAdjustmentRepository(wage_adjustment_container)
    return WageAdjustmentService(servant_repository,wage_adjustment_repository)
