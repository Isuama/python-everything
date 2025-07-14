from abc import ABC, abstractmethod
from typing import List, Optional
from core.domain.wageAdustment import WageAdjustment

class WageAdjustmentPort(ABC):
    @abstractmethod
    def get_all_wage_adjustments(self) -> List[WageAdjustment]:
        """Retrieve all wage records."""
        raise NotImplementedError

    def get_wage_adjustments_by_id(self,id:str) -> WageAdjustment:
        """Retrieve all wage records."""
        raise NotImplementedError
    
    @abstractmethod
    def add_wage_adjustments(self, data) -> None:
        """Add a new wage record."""
        raise NotImplementedError
    
    @abstractmethod
    def update_wage_adjustments(self, data) -> None:
        """Add a new wage record."""
        raise NotImplementedError

    @abstractmethod
    def delete_wage_adjustments(self, servant_id:str, wage_adjustment_id: str) -> None:
        """Update an existing wage record."""
        raise NotImplementedError
