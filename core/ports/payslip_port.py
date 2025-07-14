from abc import ABC, abstractmethod
from typing import List, Optional
from core.domain.payslip import PayslipDTO


class PayslipPort(ABC):
    @abstractmethod
    def get_all(self) -> List[PayslipDTO]:
        """Retrieve all wage records."""
        raise NotImplementedError