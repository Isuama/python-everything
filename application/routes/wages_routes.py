from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import get_servant_service,get_wage_service


wage_bp = Blueprint("wages", __name__)
servant_service = get_servant_service
wage_service = get_wage_service

@wage_bp.route("/wages", methods=["GET"])
def get_all_wages():
    servants = servant_service().get_all_active_servants()
    all_payments = wage_service().get_all_wages_with_names()
    return render_template("wages.html", active_servants=servants, all_payments=all_payments)


@wage_bp.route("/update_wages", methods=["POST"])
def update_wages():
    # try:
        servant_id = request.form.get("servant_id")
        amount = float(request.form.get("amount"))
        date = request.form.get("date")

        if not servant_id or not amount or not date:
            flash("Please fill all fields.", "danger")
            return redirect(url_for("wages.get_all_wages"))

        # Call service method to update or add wage
        wage_service().update_wage(servant_id=servant_id, amount=amount, date=date)

        flash("✅ Wage updated successfully.", "success")
    # except Exception as e:
    #     flash(f"❌ Error updating wage: {str(e)}", "danger")

        return redirect(url_for("wages.get_all_wages"))
