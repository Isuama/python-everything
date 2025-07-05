from flask import Flask
from flask_restx import Api
from application.routes.servant_routes import servant_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = "your-secret-key"

    app.register_blueprint(servant_bp)
    return app
