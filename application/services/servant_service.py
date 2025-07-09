from core.ports.servant_port import ServantPort
from core.domain.servant import Servant
from typing import List

class ServantService:
    def __init__(self, repository: ServantPort):
        self.repository = repository

    def get_servants(self) -> List[Servant]:
        return self.repository.get_all_servants()

    def create_servant(self, servant_data: dict) -> None:
        servant = Servant(**servant_data)
        self.repository.add_servant(servant)
