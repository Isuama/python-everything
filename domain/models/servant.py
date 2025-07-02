# domain/models/servant.py
from pydantic import BaseModel
from typing import Optional

class Servant(BaseModel):
    id: str
    name: str
    nickname: str
    wage: str
    isactive: bool
    photo: Optional[str] = None
    color: Optional[str] = None
