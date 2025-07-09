# domain/models/utilitySettlement.py
from pydantic import BaseModel
from typing import Optional

class UtilitySettlement(BaseModel):
    id: str
    servant_id: str
    utility_type_id: str
    amount: float
    paid_date: str

class UtilitySettlementDTo(UtilitySettlement):
    servant_name: str
    utility_type: str