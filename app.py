from flask import Flask,session
from flask_restx import Api

from application.routes.translation_routes import lang_bp
from application.routes.dashboard_routes import dashboard_bp
from application.routes.servant_routes import servant_bp
from application.routes.wage_adjustments_routes import wage_adjustments_bp

#from application.routes.attendance_routes import attendance_bp
#from application.routes.loan_routes import loan_bp
#from application.routes.wages_routes import wage_bp
#from application.routes.utility_routes import utility_bp
#from application.routes.utility_settlement_routes import utility_settlement_bp
#from application.routes.bonus_routes import bonus_bp
#from application.routes.payslip_routes import payslip_bp
from infrastructure.config.translation_config import TranslationConfig
from flask_babel import Babel, gettext as _

def create_app():
    app = Flask(__name__)
    app.secret_key = "your-secret-key"

    # Load Babel config from TranslationConfig
    app.config.from_object(TranslationConfig)
    babel = Babel(app)
    
    def get_locale():
        return session.get('lang', 'en')

    babel.init_app(app, locale_selector=get_locale)

    @app.context_processor
    def inject_locale():
        return dict(get_locale=get_locale)
    
    app.register_blueprint(lang_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(servant_bp)
    app.register_blueprint(wage_adjustments_bp)
    # app.register_blueprint(attendance_bp)
    # app.register_blueprint(loan_bp)
    # app.register_blueprint(wage_bp)
    # app.register_blueprint(utility_bp)
    # app.register_blueprint(utility_settlement_bp)
    # app.register_blueprint(bonus_bp)
    #app.register_blueprint(payslip_bp)
    
    return app