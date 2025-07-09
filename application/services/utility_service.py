from core.ports.utility_port import UtilityPort
from core.domain.utility import Utility
import uuid

class UtilityService:
    def __init__(self, utility_repo: UtilityPort):
        self.utility_repo = utility_repo

    def get_all_utilities(self) -> list[Utility]:
        return self.utility_repo.get_all_utilities()
    
    def add_utility(self, name):
        utility = Utility(
            id = str(uuid.uuid4()),
            name=name
        )
        self.utility_repo.add_utility(utility)