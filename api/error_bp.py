from flask import Flask
from .routes.error import error_bp

app = Flask(__name__)
app.register_blueprint(error_bp)
