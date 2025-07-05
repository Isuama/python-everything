from domain.ports.servant_port import ServantPort
from domain.models.servant import Servant
from infrastructure.database.cosmos import CosmosDB

class CosmosServantRepository(ServantPort):
    def __init__(self):
        db = CosmosDB()
        self.container = db.get_container(container_name="Servants", partition_key_path="/id")

    def get_all_servants(self):
        query = "SELECT c.id,c.name,c.nickname,c.wage,c.isactive,c.photo,c.color FROM c"

        return [Servant(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
    
    def get_all_active_servants(self):
        query = "SELECT * FROM c WHERE c.isactive = true"
        return [Servant(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]

    def get_active_servant_ids_and_names(self):
        query = "SELECT c.id, c.name FROM c WHERE c.isactive = true"
        return list(self.container.query_items(query, enable_cross_partition_query=True))

    def get_servant_by_id(self, servant_id: str):
        return self.container.read_item(item=servant_id, partition_key=servant_id)
    
    def add_servant(self, servant: Servant):
        self.container.create_item(servant.model_dump())

    def delete_servant(self, servant_id: str):
        self.container.delete_item(item=servant_id, partition_key=servant_id)