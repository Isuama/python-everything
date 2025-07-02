from flask import Blueprint, render_template, request, redirect, url_for
#from infrastructure.repositories.mongo_servant_repository import MongoServantRepository
from infrastructure.repositories.cosmos.servant_repository import CosmosServantRepository
from application.services.servant_service import ServantService

servant_bp = Blueprint("servant", __name__)
#repository = MongoServantRepository()
repository = CosmosServantRepository()
service = ServantService(repository)

@servant_bp.route("/servants", methods=["GET"])
def list_servants():
    servants = service.get_servants()
    return render_template("servants.html", servants=servants)

@servant_bp.route("/servants", methods=["POST"])
def add_servant():
    data = {
        "id": request.form["id"],
        "name": request.form["name"],
        "nickname": request.form["nickname"],
        "wage": float(request.form["wage"]),
        "isactive": request.form.get("isactive") == "on",
        "photo": request.form["photo"],
        "color": request.form["color"]
    }
    service.create_servant(data)
    return redirect(url_for("servant.list_servants"))