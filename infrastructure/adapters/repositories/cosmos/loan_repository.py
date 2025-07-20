from core.ports.loan_port import LoanPort
from core.domain.loan import Loan
import uuid

class CosmosLoanRepository(LoanPort):
    def __init__(self,container):
        self.container = container

    def get_all(self):
         query = "SELECT c.id, c.servant_id, c.loan_amount, c.balance, c.date_taken, c.remark FROM c"
         return [Loan(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
        # items = list(self.container.read_all_items())
        # return [Loan(**item) for item in items]

    def create(self, loan: Loan):
        self.container.create_item(loan)

    def get_by_id(self, loan_id, servant_id):
        query = """
            SELECT c.id, c.servant_id, c.loan_amount, c.balance, c.date_taken, c.remark
            FROM c
            WHERE c.id = @loan_id AND c.servant_id = @servant_id
        """

        parameters = [
            {"name": "@loan_id", "value": loan_id},
            {"name": "@servant_id", "value": servant_id}
        ]

        items = list(self.container.query_items(
            query=query,
            parameters=parameters,
            enable_cross_partition_query=True  # Optional, if partitions are unknown
        ))

        return Loan(**items[0])

    # def update(self, loan: Loan):
    #     existing = self.get_by_id(loan.id)
    #     if not existing:
    #         raise ValueError("Loan not found")

    #     self.container.upsert_item(loan.dict())
