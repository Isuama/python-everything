# container.py
from infrastructure.repositories.cosmos.servant_repository import CosmosServantRepository
from infrastructure.repositories.cosmos.wage_repository import CosmosWageRepository
from infrastructure.repositories.cosmos.utility_repository import CosmosUtilityRepository
from infrastructure.repositories.cosmos.utility_settlement_repository import CosmosUtilitySettlementRepository

from application.services.wage_service import WageService
from application.services.servant_service import ServantService
from application.services.utility_service import UtilityService
from application.services.utility_settlement_service import UtilitySettlementService

# Instantiate repositories once
servant_repo = CosmosServantRepository()
wage_repo = CosmosWageRepository()
utility_repo = CosmosUtilityRepository()
utility_settlement_repo = CosmosUtilitySettlementRepository()

# Instantiate services with injected repositories
wage_service = WageService(wage_repo=wage_repo, servant_repo=servant_repo)
servant_service = ServantService(servant_repo)
utility_service = UtilityService(utility_repo)
utility_settlement_service = UtilitySettlementService(servant_repo=servant_repo,utility_repo=utility_repo,utility_settlement_repo=utility_settlement_repo)