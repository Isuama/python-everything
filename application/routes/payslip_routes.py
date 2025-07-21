from flask import Blueprint, render_template, request, redirect, url_for, flash
from dependencies import get_servant_service , get_payslip_service

payslip_bp = Blueprint("payslip", __name__)
servant_service=get_servant_service()
payslip_service=get_payslip_service()

@payslip_bp.route("/payslip", methods=["GET", "POST"])
def get_payslip():
    servants = servant_service.get_all_active_servants()
    #attendance_dates = []
    if request.method == "POST":
            data = {
                "servant_id": request.form.get("servant"),
                "month": int(request.form.get("month")),
                "year": int(request.form.get("year"))
            }
            payslip = payslip_service.generate_payslip(**data)
            #print(payslip["selected_year"],)
            selected_year = int(request.form.get("year"))
            selected_month = int(request.form.get("month"))
            print("sett",payslip["settlements"])
            return render_template("payslip.html", servants=servants, 
                                   selected_year=selected_year,
                                   selected_month=selected_month,
                                   month_name=payslip["month_name"],
                                   servant_name=payslip["servant_name"],
                                   calendar_days = payslip["calendar_days"],
                                   attendance_dates = payslip["attendance_dates"],
                                   salary_per_day=payslip["salary_per_day"],
                                   total_attendance=payslip["total_attendance"],
                                   total_earnings=payslip["total_earnings"],
                                   adjustments=payslip["adjustments"],
                                   settlements=payslip["settlements"],
                                   total_deductions=payslip["total_deductions"],
                                   loan_capital=payslip["loan_capital"],
                                   loan_balance=payslip["loan_balance"],
                                   net_pay=payslip["net_pay"],
                                   utility_summary=payslip["utility_summary"])
    
    
    return render_template("payslip.html", servants=servants)