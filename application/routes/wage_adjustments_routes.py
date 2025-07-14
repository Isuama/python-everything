from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import get_servant_service,get_wage_adjustment_Service
from datetime import date

wage_adjustments_bp = Blueprint("wage_adjustments", __name__)
servant_service=get_servant_service()
adjustment_service=get_wage_adjustment_Service()

@wage_adjustments_bp.route("/wage_adjustments", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = {
        "servant_id": request.form.get("servant_id"),
        "amount": request.form.get("amount"),
        "adjustment_date": request.form.get("adjustment_date"),
        "remarks": request.form.get("remarks") 
       }

        adjustment_service.add_wage_adjustments(data)
        flash("Wage adjustment added successfully!", "success")
        return redirect(url_for("wage_adjustments.index"))

    adjustments = adjustment_service.get_all_wage_adjustments()
    servants = servant_service.get_all_active_servants()

    return render_template("wage_adjustments.html",
                           servants=servants,
                           adjustments=adjustments,
                           current_date=date.today().isoformat())


@wage_adjustments_bp.route("/wage_adjustments/<id>/delete", methods=["POST"])
def delete(id):
    adjustments = adjustment_service.get_wage_adjustments_by_id(id)
    if not adjustments:
        flash("Adjustment not found.", "danger")
        return redirect(url_for("wage_adjustments.index"))

    adjustment = adjustments[0]
    servant_id = adjustment.servant_id
    adjustment_service.delete_wage_adjustments(servant_id, id)

    flash("Adjustment deleted.", "success")
    return redirect(url_for("wage_adjustments.index"))


@wage_adjustments_bp.route("/wage_adjustments/<id>/edit", methods=["GET", "POST"])
def edit(id):
    print("id",id)
    adjustments = adjustment_service.get_wage_adjustments_by_id(id)
    if not adjustments:
        flash("Adjustment not found.", "danger")
        return redirect(url_for("wage_adjustments.index"))

    # Assume only one match per ID
    adjustment = adjustments[0]

    if request.method == "POST":
        data = {
            "id": id,
            "servant_id": request.form.get("servant_id"),
            "amount": request.form.get("amount"),
            "adjustment_date": request.form.get("adjustment_date"),
            "remarks": request.form.get("remarks")
        }
        adjustment_service.update_wage_adjustment(data)
        flash("Adjustment updated successfully.", "success")
        return redirect(url_for("wage_adjustments.index"))

    servants = servant_service.get_all_servants()
    return render_template("edit_wage_adjustment.html",
                           adjustment=adjustment,
                           servants=servants)
