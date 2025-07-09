from typing import List
from core.domain.servant import Servant
from core.ports.servant_port import ServantPort
from infrastructure.database.mongo import servant_collection

class MongoServantRepository(ServantPort):
    def get_all_servants(self) -> List[Servant]:
        docs = servant_collection.find()
        return [Servant(**doc) for doc in docs]

    def add_servant(self, servant: Servant) -> None:
        servant_collection.insert_one(servant.__dict__)