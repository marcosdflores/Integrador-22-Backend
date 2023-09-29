from flask import Flask, jsonify
from models.exceptions import BadRequestError, NotFoundError, ForbiddenError, ServerError

app = Flask(__name__)

# Manjeador de error para BadRequest (400)
@app.errorhandler(BadRequestError)
def handle_bad_request(error):
    response = jsonify({'error': error.message})
    response.status_code = 400
    return response

# Manjeador de error para NotFound (404)
@app.errorhandler(NotFoundError)
def handle_not_found(error):
    response = jsonify({'error': error.message})
    response.status_code = 404
    return response

# Manjeador de error para Forbidden (403)
@app.errorhandler(ForbiddenError)
def handle_forbidden(error):
    response = jsonify({'error': error.message})
    response.status_code = 403
    return response

# Manjeador de error para ServerError (500)
@app.errorhandler(ServerError)
def handle_server_error(error):
    response = jsonify({'error': error.message})
    response.status_code = 500
    return response
