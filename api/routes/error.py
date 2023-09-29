from flask import Blueprint
from exceptions import CustomException, BadRequestError, NotFoundError, ForbiddenError, ServerError

error_bp = Blueprint("errors", __name__)

@error_bp.app_errorhandler(CustomException)
def handle_custom_exception(error):
    return error.get_response()

@error_bp.app_errorhandler(400)
def handle_bad_request(error):
    return BadRequestError("User with invalid data").get_response()

@error_bp.app_errorhandler(404)
def handle_not_found(error):
    return NotFoundError("Resource not found").get_response()

@error_bp.app_errorhandler(403)
def handle_forbidden(error):
    return ForbiddenError("Permission denied").get_response()

@error_bp.app_errorhandler(500)
def handle_server_error(error):
    return ServerError("Internal server error").get_response()
