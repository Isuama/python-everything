# domain/models/bonus.py
from pydantic import BaseModel
from typing import Optional

class Bonus(BaseModel):
    id: str
    servant_id: str
    amount: float
    paid_date: str

class BonusDTO(Bonus):
    servant_name: str