from abc import ABC, abstractmethod
from typing import List
from domain.models.servant import Servant

class ServantPort(ABC):
    @abstractmethod
    def get_all_servants(self) -> List[Servant]:
        pass

    @abstractmethod
    def add_servant(self, servant: Servant) -> None:
        pass