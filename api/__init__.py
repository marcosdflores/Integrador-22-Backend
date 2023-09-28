from flask import Flask
from flask_cors import CORS
from config import Config
from .routes.auth_bp import auth_bp, users_bp

from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__)
    
    CORS(app, supports_credentials=True)
    
    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(users_bp)
    app.register_blueprint(auth_bp)

    return app