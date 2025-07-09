from abc import ABC, abstractmethod
from typing import List, Optional
from domain.models.wage import Wage


class WagePort(ABC):
    @abstractmethod
    def get_all(self) -> List[Wage]:
        """Retrieve all wage records."""
        raise NotImplementedError

    @abstractmethod
    def get_wage_by_servant_and_date(self, servant_id: str, date: str) -> Optional[Wage]:
        """Retrieve a specific wage record by servant ID and date."""
        raise NotImplementedError

    @abstractmethod
    def add(self, wage: Wage) -> None:
        """Add a new wage record."""
        raise NotImplementedError

    @abstractmethod
    def update(self, wage: Wage) -> None:
        """Update an existing wage record."""
        raise NotImplementedError
