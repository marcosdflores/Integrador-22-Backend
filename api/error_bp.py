from flask import Flask
from error import error_bp

app = Flask(__name)
app.register_blueprint(error_bp)
