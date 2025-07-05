from domain.ports.attendance_port import AttendancePort
from typing import Dict
import calendar

class AttendanceService:
    def __init__(self, repository: AttendancePort):
        self.repository = repository

    def build_attendance_lookup(self, year: int, month: int) -> Dict[int, Dict[str, bool]]:
        last_day = calendar.monthrange(year, month)[1]
        start_date = f"{year:04d}-{month:02d}-01"
        end_date = f"{year:04d}-{month:02d}-{last_day:02d}"

        records = self.repository.get_attendance_records(start_date, end_date)

        lookup = {}
        for record in records:
            day = int(record.date.split("-")[2])
            if record.present:
                lookup.setdefault(day, {})[record.servant_id] = True
        return lookup
