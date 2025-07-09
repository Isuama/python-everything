from typing import List
from domain.models.utilitySettlement import UtilitySettlement
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