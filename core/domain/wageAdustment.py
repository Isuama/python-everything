# domain/models/wage.py
from pydantic import BaseModel
from typing import Optional

class WageAdjustment(BaseModel):
    id: str
    servant_id: str
    amount: float
    adjustment_date: str
    remarks: str

class WageAdjustmentDTO(WageAdjustment):
    servant_name: str