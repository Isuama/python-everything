from typing import List
from core.domain.utilitySettlement import UtilitySettlement
from abc import ABC, abstractmethod

class UtilitySettlementPort(ABC):
    @abstractmethod
    def get_all_utility_settlements(self) -> List[UtilitySettlement]:
        """Retrieve all utility settlement records."""
        raise NotImplementedError

    @abstractmethod
    def add_utility_settlement(self, utilitySettlement: UtilitySettlement) -> None:
        """Add a new utility settlement record."""
        raise NotImplementedError
    
    @abstractmethod
    def get_utility_summary_by_servant(self,servant_id:str, start_date:str, end_date:str): pass