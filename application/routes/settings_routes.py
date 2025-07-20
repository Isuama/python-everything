from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import get_servant_service  # import instances

settings_bp = Blueprint("settings", __name__)
servant_service=get_servant_service()

@settings_bp.route("/settings", methods=["GET", "POST"])
def get_base_settings():
    servants = servant_service.get_all_active_servants()
    return render_template("settings.html", servants=servants)