from core.ports.servant_port import ServantPort
from core.domain.servant import Servant
from typing import List

class CosmosServantRepository(ServantPort):
    def __init__(self,container):
        self.container=container

    def add_servant(self, servant: Servant) -> None:
        self.container.create_item(servant)

    def update_servant(self, servant: Servant) -> None:
        self.container.replace_item(
            item=servant.id,
            body=servant.model_dump()
        )

    def delete_servant(self, servant_id: str) -> None:
        return
        #  self.container.delete_item(
        #      item=servant_id,
        #      partition_key=servant_id  # Adjust based on your partition key
        #  )

    def get_all_servants(self) -> List[Servant]:
        query = "SELECT * FROM c"
        items = list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return [Servant(**item) for item in items]
    
    def get_all_active_servants(self) -> List[Servant]:
        query = "SELECT * FROM c WHERE c.isactive = true"
        items = list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return [Servant(**item) for item in items]

    def get_active_servant_ids_and_names(self) -> List[Servant]:
        query = "SELECT c.id, c.name FROM c WHERE c.isactive = true"
        items = list(self.container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        return [Servant(id=item["id"], name=item["name"]) for item in items]

    def get_servant_by_id(self, servant_id: str) -> Servant:
        response = self.container.read_item(
            item=servant_id,
            partition_key=servant_id
        )
        return Servant(**response)
    
    