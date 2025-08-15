from pydantic import BaseModel

class Settlement(BaseModel):
    id: str
    servant_id: str
    loan_id: str
    settled_amount: float
    settled_date: str
