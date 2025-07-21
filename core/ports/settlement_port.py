from typing import List
from core.domain.settlement import Settlement

class SettlementPort:
    def get_all(self) -> List[Settlement]: pass
    def get_settlement_by_servant(self,servant_id:str, start_date:str, end_date:str): pass
    def create(self, settlement: Settlement): pass
