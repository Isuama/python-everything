from core.ports.loan_port import LoanPort
from core.domain.loan import Loan
from infrastructure.database.cosmos import CosmosDB
import uuid

class CosmosLoanRepository(LoanPort):
    def __init__(self):
        self.container = CosmosDB().get_container("Loans", partition_key_path="/servant_id")

    def get_all(self):
         query = "SELECT c.id, c.servant_id, c.loan_amount, c.balance, c.date_taken, c.remark FROM c"
         return [Loan(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]
        # items = list(self.container.read_all_items())
        # return [Loan(**item) for item in items]

    def create(self, loan: Loan):
        self.container.create_item(vars(loan))

    def get_by_id(self, loan_id, servant_id):
        item = self.container.read_item(item=loan_id, partition_key=servant_id)
        return Loan(**item)

    def update(self, loan: Loan):
        self.container.replace_item(item=loan.id, body=vars(loan))
