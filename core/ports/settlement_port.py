from typing import List
from core.domain.settlement import Settlement

class SettlementPort:
    def get_all(self) -> List[Settlement]: pass
    def create(self, settlement: Settlement): pass
