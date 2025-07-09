from typing import List
from domain.models.utility import Utility
from abc import ABC, abstractmethod

class UtilityPort(ABC):
    @abstractmethod
    def get_all_utilities(self) -> List[Utility]:
        """Retrieve all utility records."""
        raise NotImplementedError

    @abstractmethod
    def add_utility(self, utility: Utility) -> None:
        """Add a new utility record."""
        raise NotImplementedError