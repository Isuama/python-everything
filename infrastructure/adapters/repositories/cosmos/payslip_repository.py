from core.ports.payslip_port import PayslipPort
from core.domain.servant import Servant

class CosmosPayslipRepository(PayslipPort):
    def __init__(self,container):
        self.container = container

    def get_all(self):
        query = "SELECT c.id, c.name, c.nickname, c.wage, c.isactive, c.photo, c.color FROM c"

        return [Servant(**item) for item in self.container.query_items(query, enable_cross_partition_query=True)]