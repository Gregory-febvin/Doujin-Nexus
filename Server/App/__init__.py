# app/__init__.py
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Import and register blueprints
    from .general_endpoints import general_bp
    from .browsing_section import browsing_bp
    from .language_change import language_bp
    from .search_functionality import search_bp
    from .image_handle import image_bp

    app.register_blueprint(general_bp)
    app.register_blueprint(browsing_bp)
    app.register_blueprint(language_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(image_bp)

    return app
