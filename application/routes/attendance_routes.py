from flask import Blueprint, render_template, request
from application.services.attendance_service import AttendanceService
from infrastructure.repositories.cosmos.attendance_repository import CosmosAttendanceRepository
from infrastructure.database.cosmos import CosmosDB
from utils.calendar_utils import get_calendar, get_weekday_labels
from datetime import datetime
import calendar

attendance_bp = Blueprint("attendance", __name__)
attendance_service = AttendanceService(CosmosAttendanceRepository())

# You might already have this shared somewhere:
db = CosmosDB()
servants_container = db.get_container(container_name="Servants", partition_key_path="/id")

@attendance_bp.route("/attendance",endpoint="attendance")
def view_attendance():
    now = datetime.now()
    year = request.args.get('year', default=now.year, type=int)
    month = request.args.get('month', default=now.month, type=int)

    month_days = get_calendar(year, month)
    month_name = calendar.month_name[month]

    all_servants = list(servants_container.read_all_items())
    active_servants = [s for s in all_servants if s.get("isactive")]

    attendance_lookup = attendance_service.build_attendance_lookup(year, month)
    weekday_labels = get_weekday_labels()
    return render_template('calendar.html',
                           weekday_labels=weekday_labels,
                           year=year,
                           month=month,
                           month_name=month_name,
                           month_days=month_days,
                           today=now.day if (year == now.year and month == now.month) else None,
                           servants=active_servants,
                           attendance=attendance_lookup)

@attendance_bp.route("/save_attendance",endpoint="save_attendance")
def view_attendance():
    return True