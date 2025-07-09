from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import servant_service,bonus_service  # import instances

bonus_bp = Blueprint("Bonus", __name__)

@bonus_bp.route("/bonuses", methods=["GET"])
def get_all_bonuses():
    servants = servant_service.get_servants()
    bonuses = bonus_service.get_all_bonuses()

    return render_template("bonuses.html", servants=servants,bonuses=bonuses)

@bonus_bp.route("/bonuses", methods=["POST"])
def add_bonus():
    
    servant_id = request.form["servant_id"]
    amount = float(request.form["amount"])
    paid_date = request.form["paid_date"]

    bonus_service.add_bonus(servant_id,amount,paid_date)

    return redirect(url_for("Bonus.get_all_bonuses"))