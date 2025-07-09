from dataclasses import dataclass

@dataclass
class Settlement:
    id: str
    servant_id: str
    loan_id: str
    settled_amount: float
    settled_date: str
