from flask import Flask
from flask_restx import Api
from application.routes.servant_routes import servant_bp
from application.routes.attendance_routes import attendance_bp
from application.routes.loan_routes import loan_bp
from application.routes.wages_routes import wage_bp
from application.routes.utility_routes import utility_bp
from application.routes.utility_settlement_routes import utility_settlement_bp
from application.routes.bonus_routes import bonus_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "your-secret-key"

    app.register_blueprint(servant_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(loan_bp)
    app.register_blueprint(wage_bp)
    app.register_blueprint(utility_bp)
    app.register_blueprint(utility_settlement_bp)
    app.register_blueprint(bonus_bp)
 
    return app
