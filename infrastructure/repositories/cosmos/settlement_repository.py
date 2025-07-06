from domain.ports.settlement_port import SettlementPort
from domain.models.settlement import Settlement
from infrastructure.database.cosmos import CosmosDB

class CosmosSettlementRepository(SettlementPort):
    def __init__(self):
        self.container = CosmosDB().get_container("LoanSettlements", partition_key_path="/servant_id")

    def get_all(self):
        query = "SELECT c.id, c.servant_id, c.loan_id, c.settled_amount, c.settled_date FROM c"
        return [Settlement(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
        #items = list(self.container.read_all_items())
        #return [Settlement(**item) for item in items]

    def create(self, settlement: Settlement):
        self.container.create_item(vars(settlement))
