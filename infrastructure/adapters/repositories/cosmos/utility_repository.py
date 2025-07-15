from core.ports.utility_port import UtilityPort
from core.domain.utility import Utility
import uuid

class CosmosUtilityRepository(UtilityPort):
    def __init__(self,container):
        self.container = container

    def get_all_utilities(self):
         query = "SELECT c.id, c.name FROM c"
         return [Utility(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
    
    def add_utility(self, utility: Utility):
        self.container.create_item(utility.model_dump())