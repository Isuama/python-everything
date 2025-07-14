from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import get_utility_service


utility_bp = Blueprint("utility", __name__)
utility_service=get_utility_service()

@utility_bp.route("/utility", methods=["GET"])
def get_all_utilities():
    utilities = utility_service.get_all_utilities()
    return render_template("utility.html", utilities=utilities)

@utility_bp.route("/addUtility", methods=["POST"])
def add_utility():
    name = request.form.get("name")
    utility_service.add_utility(name)
    return redirect(url_for("utility.get_all_utilities"))