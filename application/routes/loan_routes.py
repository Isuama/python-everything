from flask import Blueprint, render_template, request, redirect, url_for, flash
from application.services.loan_service import LoanService
from infrastructure.adapters.repositories.cosmos.loan_repository import CosmosLoanRepository
from infrastructure.adapters.repositories.cosmos.settlement_repository import CosmosSettlementRepository
from infrastructure.database.cosmos import CosmosDB

loan_bp = Blueprint("loan", __name__)
loan_service = LoanService(CosmosLoanRepository(), CosmosSettlementRepository())
db = CosmosDB()

@loan_bp.route("/loan")
def loan():
    servants = list(db.get_container("Servants", "/id").query_items(
        query="SELECT c.id, c.name FROM c WHERE c.isactive = true",
        enable_cross_partition_query=True
    ))
    loans = loan_service.get_loans()
    settlements = loan_service.get_settlements()
    return render_template("loans.html", servants=servants, loans=loans, settlements=settlements)

@loan_bp.route("/loan", methods=["POST"])
def add_loan_or_settlement():
    form_type = request.form.get("formType")
    servant_id = request.form.get("servant_id")
    servant_name = request.form.get("servant_name")

    if form_type == "loan":
        amount = float(request.form.get("loanAmount"))
        date_taken = request.form.get("loanDate")
        remark = request.form.get("loanRemark")
        loan_service.create_loan(servant_id, amount, date_taken, remark)
        flash("✅ Loan added successfully.", "success")

    elif form_type == "settlement":
        settled_amount = float(request.form.get("settledAmount"))
        settled_date = request.form.get("settledDate")
        loan_id = request.form.get("loan_id")
        loan_service.create_settlement(servant_id, loan_id, settled_amount, settled_date)
        flash("✅ Loan settlement added.", "success")

    return redirect(url_for("loan.loan"))
