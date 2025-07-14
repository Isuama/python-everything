from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import get_servant_service
from datetime import datetime,timedelta

dashboard_bp = Blueprint("Dashboard", __name__)
servant_service=get_servant_service()

@dashboard_bp.route("/", methods=["GET"])
def dashboard():
    servants = servant_service.get_servants()
    weekly_wages = []
    # Get week offset from URL query params or default to 0
    week_offset = int(request.args.get("week_offset", 0))
    #print(week_offset)
    # Calculate the Monday of the current week
    today = datetime.today()
    current_monday = today - timedelta(days=today.weekday())
    # Apply offset to get target week's Monday
    target_monday = current_monday + timedelta(weeks=week_offset)
    target_sunday = target_monday + timedelta(days=6)

    # Format dates for display
    monday_str = target_monday.strftime("%Y-%m-%d")
    sunday_str = target_sunday.strftime("%Y-%m-%d")
    monday = monday_str
    sunday = sunday_str
    current_date = today.strftime("%Y-%m-%d")

    return render_template("dashboard.html",
                               weekly_wages=weekly_wages,
                               monday=monday,
                               sunday=sunday,
                               current_date=current_date,
                               week_offset=week_offset)