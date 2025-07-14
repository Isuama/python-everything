from flask import Blueprint, render_template, request, redirect, url_for
#from infrastructure.repositories.mongo_servant_repository import MongoServantRepository
from infrastructure.adapters.repositories.cosmos.servant_repository import CosmosServantRepository
from application.services.servant_service import ServantService
from dependencies import get_servant_service

servant_bp = Blueprint("servant", __name__)
service = get_servant_service()

@servant_bp.route("/servants", methods=["GET"])
def list_servants():
    servants = service.get_all_servants()
    return render_template("servants.html", servants=servants)

@servant_bp.route("/servants/add", methods=["POST"])
def add_servant():
    data = {
        "name": request.form["name"],
        "nickname": request.form["nickname"],
        "wage": request.form["wage"],
        "isactive": request.form.get("isactive") == "on",
        "photo": "",#request.form["photo"],
        "color": request.form["color"]
    }
    service.add_servant(data)
    return redirect(url_for("servant.list_servants"))

@servant_bp.route("/servants/delete/<servant_id>", methods=["POST"])
def delete_servant(servant_id):
    service.delete_servant(servant_id)
    return redirect(url_for("servant.list_servants"))