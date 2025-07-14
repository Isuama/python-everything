from core.ports.servant_port import ServantPort
from core.domain.servant import Servant
from typing import List
from datetime import datetime
import uuid
from infrastructure.utils.cast_utils import safe_float

class ServantService:
    def __init__(self, repository: ServantPort):
        self.repository = repository

    def add_servant(self, data) -> None:
        servant = {
            "id": str(uuid.uuid4()),
            "name": data["name"],
            "nickname": data.get("nickname", ""),
            "wage": safe_float(data.get("wage", 0)),
            "photo": data.get("photo", ""),
            "color": data.get("color", "#FFFFFF"),
            "isactive": data.get("isactive",False)
        }
        self.repository.add_servant(servant)

    def update_servant(self, servant: Servant) -> None:
        self.repository.update_servant(servant)

    def delete_servant(self, servant_id: str) -> None:
        self.repository.delete_servant(servant_id)

    def get_servant_by_id(self, servant_id: str) -> Servant:
        return self.repository.get_servant_by_id(servant_id)

    def get_all_servants(self) -> List[Servant]:
        return self.repository.get_all_servants()

    def get_all_active_servants(self) -> List[Servant]:
        return self.repository.get_all_active_servants()

    def get_active_servant_ids_and_names(self) -> List[Servant]:
        return self.repository.get_active_servant_ids_and_names()