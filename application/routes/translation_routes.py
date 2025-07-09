# application/routes/translation_routes.py

from flask import Blueprint, session, request, redirect, url_for, current_app

lang_bp = Blueprint('lang', __name__)

@lang_bp.route('/set_language')
def set_language():
    lang_code = request.args.get('lang')
    if lang_code in current_app.config['LANGUAGES']:
        session['lang'] = lang_code
    return redirect(request.referrer or url_for('dashboard.dashboard'))
