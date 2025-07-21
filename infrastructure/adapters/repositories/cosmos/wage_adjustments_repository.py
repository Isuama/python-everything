from core.domain.wageAdustment import WageAdjustment
from core.ports.wage_adjustment_port import WageAdjustmentPort
import uuid

class CosmosWageAdjustmentRepository(WageAdjustmentPort):
    def __init__(self,container):
        self.container = container

    def get_all_wage_adjustments(self):
         query = """
            SELECT c.id, c.servant_id, c.amount, c.adjustment_date, c.remarks
            FROM c
            ORDER BY c.adjustment_date DESC
        """
         return [WageAdjustment(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
    
    def get_wage_adjustments_by_id(self, id: str):
        query = """
            SELECT c.id, c.servant_id, c.amount, c.adjustment_date, c.remarks
            FROM c
            WHERE c.id = @id
        """
        parameters = [{"name": "@id", "value": id}]
        return [
            WageAdjustment(**item)
            for item in self.container.query_items(
                query=query,
                parameters=parameters,
                enable_cross_partition_query=True
            )
        ]
    
    def get_wage_adjustments_by_id(self,servant_id, start_date, end_date):
        query = """
            SELECT c.id, c.servant_id, c.amount, c.adjustment_date, c.remarks
            FROM c
            WHERE c.servant_id = @sid
            AND c.adjustment_date >= @start AND c.adjustment_date < @end
            ORDER BY c.date
        """
        params = [
            {"name": "@sid", "value": servant_id},
            {"name": "@start", "value": start_date.strftime("%Y-%m-%d")},
            {"name": "@end", "value": end_date.strftime("%Y-%m-%d")},
        ]
        result = self.container.query_items(query=query, parameters=params, enable_cross_partition_query=True)
        return [
        {
          "adjustment_date": record["adjustment_date"],
          "amount": record["amount"]
        }
        for record in result]
    
    def add_wage_adjustments(self, wageAdjustment:WageAdjustment):
        self.container.create_item(wageAdjustment)

    def update_wage_adjustments(self, adjustment: WageAdjustment):
        # Read the existing item first to get the partition key (assume servant_id)
        existing = self.get_wage_adjustments_by_id(adjustment.id)
        if not existing:
            raise ValueError("Adjustment not found")

        self.container.upsert_item(adjustment.dict())

    def delete_wage_adjustments(self, servant_id:str, wage_adjustments_id: str) -> None:
         self.container.delete_item(
             item=wage_adjustments_id,
             partition_key=servant_id
         )