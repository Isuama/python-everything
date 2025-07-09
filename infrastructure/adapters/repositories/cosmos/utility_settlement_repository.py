from core.ports.utility_settlement_port import UtilitySettlementPort
from core.domain.utilitySettlement import UtilitySettlement
from infrastructure.database.cosmos import CosmosDB
import uuid

class CosmosUtilitySettlementRepository(UtilitySettlementPort):
    def __init__(self):
        self.container = CosmosDB().get_container("UtilitySettlement", partition_key_path="/servant_id")

    def get_all_utility_settlements(self):
         query = "SELECT c.id, c.servant_id, c.utility_type_id, c.amount, c.paid_date FROM c ORDER BY c.paid_date DESC"
         return [UtilitySettlement(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
    
    def add_utility_settlement(self, utilitySettlement:UtilitySettlement):
        self.container.create_item(utilitySettlement.model_dump())