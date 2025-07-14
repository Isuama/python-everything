from flask import Blueprint, render_template, request, redirect, url_for, flash
#from dependencies import payslip_service, servant_service  # import instances

payslip_bp = Blueprint("payslip", __name__)


@payslip_bp.route("/payslip", methods=["GET", "POST"])
def get_payslip():
    return
    #servants = servant_service.get_servants()
   
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

        