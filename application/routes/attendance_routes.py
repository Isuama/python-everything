from flask import Blueprint, render_template, request, flash, redirect, url_for
from application.services.attendance_service import AttendanceService
from infrastructure.adapters.repositories.cosmos.attendance_repository import CosmosAttendanceRepository
from infrastructure.database.cosmos import CosmosDB
from infrastructure.utils.calendar_utils import get_calendar, get_weekday_labels
from datetime import datetime
import calendar
from dependencies import get_servant_service,get_attendance_Service

attendance_bp = Blueprint("attendance", __name__)
servant_service=get_servant_service()
attendance_service=get_attendance_Service()

@attendance_bp.route("/attendance",endpoint="attendance")
def view_attendance():
    now = datetime.now()
    year = request.args.get('year', default=now.year, type=int)
    month = request.args.get('month', default=now.month, type=int)

    month_days = get_calendar(year, month)
    month_name = calendar.month_name[month]

    #all_servants = list(get_servant_service().get_all_servants())
    #active_servants = [s for s in all_servants if s.get("isactive")]
    active_servants = get_servant_service().get_all_active_servants();

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

@attendance_bp.route("/save_attendance", methods=["POST"])
def save_attendance():
    try:
        year = int(request.form["year"])
        month = int(request.form["month"])
        form_data = request.form.to_dict(flat=False)

        attendance_service.save_attendance(year, month, form_data)

        flash("✅ Attendance saved successfully!", "success")
    except Exception as e:
        flash(f"❌ Error saving attendance: {str(e)}", "danger")

    return redirect(url_for("attendance.attendance", year=year, month=month))
