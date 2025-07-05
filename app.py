from flask import Flask
from flask_restx import Api
from application.routes.servant_routes import servant_bp
from application.routes.attendance_routes import attendance_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "your-secret-key"

    app.register_blueprint(servant_bp)
    app.register_blueprint(attendance_bp)
    return app
