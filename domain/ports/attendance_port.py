from typing import List
from datetime import date
from domain.models.attendance import Attendance

class AttendancePort:
    def get_attendance_records(self, start_date: str, end_date: str) -> List[Attendance]:
        raise NotImplementedError
