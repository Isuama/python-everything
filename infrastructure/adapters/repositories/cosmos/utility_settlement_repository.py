from collections import defaultdict
from core.ports.utility_settlement_port import UtilitySettlementPort
from core.domain.utilitySettlement import UtilitySettlement
import uuid

class CosmosUtilitySettlementRepository(UtilitySettlementPort):
    def __init__(self,container):
        self.container = container

    def get_all_utility_settlements(self):
         query = "SELECT c.id, c.servant_id, c.utility_type_id, c.amount, c.paid_date FROM c ORDER BY c.paid_date DESC"
         return [UtilitySettlement(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
    
    def add_utility_settlement(self, utilitySettlement:UtilitySettlement):
        self.container.create_item(utilitySettlement.model_dump())

    def get_utility_summary_by_servant(self, servant_id, start_date, end_date):
        # Query settlements for this servant
        query = """
            SELECT * FROM c 
            WHERE c.servant_id = @servant_id AND c.paid_date >= @start_date AND c.paid_date <= @end_date
        """
        params = [
            {"name": "@servant_id", "value": servant_id},
            {"name": "@start_date", "value": start_date.strftime("%Y-%m-%d")},
            {"name": "@end_date", "value": end_date.strftime("%Y-%m-%d")},
        ]

        settlements = list(self.container.query_items(
            query=query,
            parameters=params,
            enable_cross_partition_query=True
        ))
        return settlements