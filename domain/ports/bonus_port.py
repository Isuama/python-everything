from typing import List
from domain.models.bonus import Bonus,BonusDTO
from abc import ABC, abstractmethod

class BonusPort(ABC):
    @abstractmethod
    def get_all_bonuses(self) -> List[BonusDTO]:
        """Retrieve all paid bonuses records."""
        raise NotImplementedError

    @abstractmethod
    def add_bonus(self, bonus: Bonus) -> None:
        """Add a new bonus record."""
        raise NotImplementedError