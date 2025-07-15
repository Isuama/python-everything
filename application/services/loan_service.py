from core.ports.servant_port import ServantPort
from core.ports.loan_port import LoanPort
from core.ports.settlement_port import SettlementPort
from core.domain.loan import Loan
from core.domain.settlement import Settlement
import uuid

class LoanService:
    def __init__(self, loan_repository:LoanPort, settlement_repository: SettlementPort):
        self.loan_repository = loan_repository
        self.settlement_repository = settlement_repository

    def get_loans(self):
        return self.loan_repository.get_all()

    def get_settlements(self):
        setts = self.settlement_repository.get_all()
        return setts

    def create_loan(self, servant_id, amount, date_taken, remark):
        loan = Loan(
            id=str(uuid.uuid4()),
            servant_id=servant_id,
            loan_amount=amount,
            balance=amount,
            date_taken=date_taken,
            remark=remark
        )
        self.loan_repository.create(loan)

    def create_settlement(self, servant_id, loan_id, settled_amount, settled_date):
        settlement = Settlement(
            id=str(uuid.uuid4()),
            servant_id=servant_id,
            loan_id=loan_id,
            settled_amount=settled_amount,
            settled_date=settled_date
        )
        self.settlement_repository.create(settlement)

        loan = self.loan_repository.get_by_id(loan_id, servant_id)
        loan.balance -= settled_amount
        self.loan_repository.update(loan)
