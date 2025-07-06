from domain.ports.loan_port import LoanPort
from domain.ports.settlement_port import SettlementPort
from domain.models.loan import Loan
from domain.models.settlement import Settlement
import uuid

class LoanService:
    def __init__(self, loan_repo: LoanPort, settlement_repo: SettlementPort):
        self.loan_repo = loan_repo
        self.settlement_repo = settlement_repo

    def get_loans(self):
        return self.loan_repo.get_all()

    def get_settlements(self):
        return self.settlement_repo.get_all()

    def create_loan(self, servant_id, amount, date_taken, remark):
        loan = Loan(
            id=str(uuid.uuid4()),
            servant_id=servant_id,
            loan_amount=amount,
            balance=amount,
            date_taken=date_taken,
            remark=remark
        )
        self.loan_repo.create(loan)

    def create_settlement(self, servant_id, loan_id, settled_amount, settled_date):
        settlement = Settlement(
            id=str(uuid.uuid4()),
            servant_id=servant_id,
            loan_id=loan_id,
            settled_amount=settled_amount,
            settled_date=settled_date
        )
        self.settlement_repo.create(settlement)

        loan = self.loan_repo.get_by_id(loan_id, servant_id)
        loan.balance -= settled_amount
        self.loan_repo.update(loan)
