from typing import List
from domain.models.settlement import Settlement

class SettlementPort:
    def get_all(self) -> List[Settlement]: pass
    def create(self, settlement: Settlement): pass
