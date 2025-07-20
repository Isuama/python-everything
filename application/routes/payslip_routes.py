from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import get_servant_service  # import instances

payslip_bp = Blueprint("payslip", __name__)
servant_service=get_servant_service()

@payslip_bp.route("/payslip", methods=["GET", "POST"])
def get_payslip():
    servants = servant_service.get_all_active_servants()
    return render_template("payslip.html", servants=servants)
    # if request.method == "POST":
    #         data = {
    #             "servant_id": request.form.get("servant"),
    #             "month": int(request.form.get("month")),
    #             "year": int(request.form.get("year"))
    #         }
    #         print(data)
    #         result = payslip_service.generate_payslip(**data)
    #         return render_template("payslip.html", servants=servants, **result)
    #return render_template("payslip.html", servants=servants)

        