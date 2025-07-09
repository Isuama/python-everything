from core.ports.attendance_port import AttendancePort
from typing import Dict
import calendar
import uuid

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

    def save_attendance(self, year: int, month: int, form_data: Dict[str, list]):
        # Build set of checked (day, servant_id)
        checked_attendance = set()
        for key in form_data:
            if key.startswith("attendance["):
                parts = key.split("[")
                day = int(parts[1].rstrip("]"))
                servant_id = parts[2].rstrip("]")
                checked_attendance.add((day, servant_id))

        # Build date range
        last_day = calendar.monthrange(year, month)[1]
        start_date = f"{year:04d}-{month:02d}-01"
        end_date = f"{year:04d}-{month:02d}-{last_day:02d}"

        existing_records = self.repository.get_attendance_records(start_date, end_date)

        # Build existing set
        existing_set = set()
        id_map = {}
        for rec in existing_records:
            day = int(rec.date.split("-")[2])
            servant_id = rec.servant_id
            existing_set.add((day, servant_id))
            id_map[(day, servant_id)] = rec.id

        # Create new attendance
        for day, servant_id in checked_attendance - existing_set:
            record_date = f"{year:04d}-{month:02d}-{day:02d}"
            self.repository.create_attendance({
                "id": str(uuid.uuid4()),
                "servant_id": servant_id,
                "date": record_date,
                "present": True
            })

        # Delete unchecked attendance
        for day_servant in existing_set - checked_attendance:
            rec_id = id_map[day_servant]
            servant_id = day_servant[1]
            self.repository.delete_attendance(rec_id, servant_id)
