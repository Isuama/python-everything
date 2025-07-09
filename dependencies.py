# container.py
from infrastructure.repositories.cosmos.servant_repository import CosmosServantRepository
from infrastructure.repositories.cosmos.wage_repository import CosmosWageRepository
from application.services.wage_service import WageService
from application.services.servant_service import ServantService

# Instantiate repositories once
servant_repo = CosmosServantRepository()
wage_repo = CosmosWageRepository()

# Instantiate services with injected repositories
wage_service = WageService(wage_repo=wage_repo, servant_repo=servant_repo)
servant_service = ServantService(servant_repo)
