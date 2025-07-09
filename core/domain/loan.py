from dataclasses import dataclass

@dataclass
class Loan:
    id: str
    servant_id: str
    loan_amount: float
    balance: float
    date_taken: str
    remark: str = ""
