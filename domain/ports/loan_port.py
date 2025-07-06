from typing import List
from domain.models.loan import Loan

class LoanPort:
    def get_all(self) -> List[Loan]: pass
    def create(self, loan: Loan): pass
    def get_by_id(self, loan_id: str, servant_id: str) -> Loan: pass
    def update(self, loan: Loan): pass
