# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints
    from .general_endpoints import general_bp
    from .browsing_section import browsing_bp
    from .language_change import language_bp
    from .search_functionality import search_bp

    app.register_blueprint(general_bp)
    app.register_blueprint(browsing_bp)
    app.register_blueprint(language_bp)
    app.register_blueprint(search_bp)

    return app
