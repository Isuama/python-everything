from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import get_servant_service  # import instances

prediction_bp = Blueprint("prediction", __name__)
servant_service=get_servant_service()

@prediction_bp.route("/prediction", methods=["GET", "POST"])
def get_base_prediction():
    servants = servant_service.get_all_active_servants()
    return render_template("prediction.html", servants=servants)