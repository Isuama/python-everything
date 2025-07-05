from pydantic import BaseModel

class Attendance(BaseModel):
    id: str
    servant_id: str
    date: str
    present: bool
