from core.ports.wage_port import WagePort
from core.domain.wage import Wage
from infrastructure.database.cosmos import CosmosDB

class CosmosWageRepository(WagePort):
    def __init__(self,container):
        self.container = container

    def add(self, wage: Wage):
        self.container.create_item(wage.model_dump())

    def update(self, wage: Wage):
        print("updating",wage.model_dump())
        self.container.replace_item(
            item=wage.id,
            body=wage.model_dump()
        )


    def get_wage_by_servant_and_date(self, servant_id: str, date: str):
        query = f"""
            SELECT * FROM c
            WHERE c.servant_id = @servant_id AND c.date = @date
        """
        params = [
            {"name": "@servant_id", "value": servant_id},
            {"name": "@date", "value": date}
        ]
        items = list(self.container.query_items(
            query=query,
            parameters=params,
            enable_cross_partition_query=True
        ))

        if items:
            return Wage(**items[0])
        return None

    def get_all(self):
        query = "SELECT c.id, c.servant_id, c.amount, c.date FROM c ORDER BY c.date DESC"
        return [Wage(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
