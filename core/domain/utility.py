# domain/models/utility.py
from pydantic import BaseModel
from typing import Optional

class Utility(BaseModel):
    id: str
    name: str