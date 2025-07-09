# domain/models/utilitySettlement.py
from pydantic import BaseModel
from typing import Optional

class Dashboard(BaseModel):
    id: str
    servant_id: str
    amount: float
    paid_date: str

class DashboardDTO(Dashboard):
    servant_name: str