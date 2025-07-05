from abc import ABC, abstractmethod
from typing import List, Dict

class AttendancePort(ABC):
    @abstractmethod
    def get_attendance_records(self, start_date: str, end_date: str) -> List:
        pass

    @abstractmethod
    def create_attendance(self, record: Dict):
        pass

    @abstractmethod
    def delete_attendance(self, item_id: str, servant_id: str):
        pass
