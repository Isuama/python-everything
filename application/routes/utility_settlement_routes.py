from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import servant_service,utility_service,utility_settlement_service  # import instances
from utils.date_utils import get_current_date


utility_settlement_bp = Blueprint("utilitySettlement", __name__)


@utility_settlement_bp.route("/utility_settlement", methods=["GET"])
def get_all_utilitySettlements():
    servants = servant_service.get_servants()
    utilities = utility_service.get_all_utilities()
    settlements = utility_settlement_service.get_all_utility_settlements()

    return render_template("utilitySettlement.html", 
                               servants=servants, 
                               utilities=utilities, 
                               utility_history=settlements,
                               current_date=get_current_date())

@utility_settlement_bp.route("/add_utility_settlement", methods=["POST"])
def add_utility():
    
    servant_id = request.form["servant_id"]
    utility_type_id = request.form["utility_type"]
    amount = float(request.form["amount"])
    paid_date = request.form["paid_date"]

    utility_settlement_service.add_utility_settlement(servant_id,utility_type_id,amount,paid_date)
    return redirect(url_for("utilitySettlement.get_all_utilitySettlements"))