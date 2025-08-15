from pydantic import BaseModel

class Loan(BaseModel):
    id: str
    servant_id: str
    loan_amount: float
    balance: float
    date_taken: str
    remark: str = ""
