from core.ports.settlement_port import SettlementPort
from core.domain.settlement import Settlement
from infrastructure.database.cosmos import CosmosDB

class CosmosSettlementRepository(SettlementPort):
    def __init__(self,container):
        self.container = container

    def get_all(self):
        query = "SELECT c.id, c.servant_id, c.loan_id, c.settled_amount, c.settled_date FROM c"
        return [Settlement(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
        #items = list(self.container.read_all_items())
        #return [Settlement(**item) for item in items]
    def create(self, settlement: Settlement):
        self.container.create_item(vars(settlement))

    def get_settlement_by_servant(self,servant_id, start_date, end_date):
        query = """
            SELECT c.settled_date,c.settled_amount 
            FROM c 
            WHERE c.servant_id = @sid
            AND c.settled_date >= @start AND c.settled_date < @end
            ORDER BY c.settled_date
        """
        params = [
            {"name": "@sid", "value": servant_id},
            {"name": "@start", "value": start_date.strftime("%Y-%m-%d")},
            {"name": "@end", "value": end_date.strftime("%Y-%m-%d")},
        ]
        result = self.container.query_items(query=query, parameters=params, enable_cross_partition_query=True)

        # for record in result:
        #     print("Record:", record)
        #     # Or just print the specific field you're interested in
        #     print("Settled Date:", record.get("settled_date"))

        return [
        {
          "settled_date": record["settled_date"],
          "settled_amount": record["settled_amount"]
        }
        for record in result]
