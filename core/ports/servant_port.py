from abc import ABC, abstractmethod
from typing import List
from core.domain.servant import Servant

class ServantPort(ABC):

    @abstractmethod
    def add_servant(self, servant: Servant) -> None:
        pass

    @abstractmethod
    def update_servant(self, servant: Servant) -> None:
        pass

    @abstractmethod
    def delete_servant(self, servant_id: str) -> None:
        pass

    @abstractmethod
    def get_all_servants(self) -> List[Servant]:
        pass

    @abstractmethod
    def get_all_active_servants(self) -> List[Servant]:
        pass

    @abstractmethod
    def get_active_servant_ids_and_names(self) -> List[Servant]:
        pass

    @abstractmethod
    def get_servant_by_id(self, servant_id: str) -> Servant:
        pass