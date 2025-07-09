# domain/models/wage.py
from pydantic import BaseModel
from typing import Optional

class Wage(BaseModel):
    id: str
    servant_id: str
    amount: float
    date: str

class WageWithServantName(Wage):
    name: str