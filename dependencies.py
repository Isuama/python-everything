#db
from infrastructure.database.cosmos import CosmosDB
from infrastructure.adapters.container_registry.cosmos_container_registry import CosmosContainerRegistry

# repositories
from infrastructure.adapters.repositories.cosmos.servant_repository import CosmosServantRepository
from infrastructure.adapters.repositories.cosmos.wage_repository import CosmosWageRepository
from infrastructure.adapters.repositories.cosmos.utility_repository import CosmosUtilityRepository
from infrastructure.adapters.repositories.cosmos.utility_settlement_repository import CosmosUtilitySettlementRepository
from infrastructure.adapters.repositories.cosmos.bonus_repository import CosmosBonusRepository
from infrastructure.adapters.repositories.cosmos.attendance_repository import CosmosAttendanceRepository
#from infrastructure.repositories.cosmos.dashboard_repository import DashboardRepository

# services
from application.services.servant_service import ServantService
from application.services.wage_service import WageService
from application.services.utility_service import UtilityService
from application.services.utility_settlement_service import UtilitySettlementService
from application.services.bonus_service import BonusService
from application.services.attendance_service import AttendanceService
#from application.services.dashboard_service import DashboardService
#from application.services.payslip_service import PayslipService

# Create CosmosDB only once
db_instance = CosmosDB()
registry = CosmosContainerRegistry(db_instance)

def get_servant_service():
    servant_container = registry.get("servants")
    repository = CosmosServantRepository(servant_container)
    return ServantService(repository)

def get_wage_service():
    wage_container = registry.get("wages")
    repository = CosmosWageRepository(wage_container)
    return WageService(repository)

def get_utility_service():
    utility_container = registry.get("utility")
    repository = CosmosUtilityRepository(utility_container)
    return UtilityService(repository)

def get_utility_settlement_service():
    utility_settlement_container = registry.get("utility")
    repository = CosmosUtilitySettlementRepository(utility_settlement_container)
    return UtilitySettlementService(repository)
