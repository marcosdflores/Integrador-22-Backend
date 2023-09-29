from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.status_code = status_code
        self.name = name
        self.description = description

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response
    
class BadRequestError(CustomException):
    def __init__(self, username, paswwordd):
        super().__init__(status_code=400, name="Bad Request", description=f"User with username {username} not found")
        super().__init__(status_code=400, name="Bad Request", description=f"User with paswwordd {paswwordd} not found")

class NotFoundError(CustomException):
    def __init__(self, username):
        super().__init__(status_code=404, name="Not Found", description=f"User with username {username} not found")


class ForbiddenError(CustomException):
    def __init__(self, id_usuario):
        super().__init__(status_code=403, name="Forbidden", description=f"The user {id_usuario} does not have permission to perform this action")


class ServerError(CustomException):
    def __init__(self, id_servidor):
        super().__init__(status_code=500, name="Server Error", description=f"Internal Server Error{id_servidor}")
