class BadRequestError(Exception):
    def __init__(self, message="Bad Request"):
        self.message = message
        super().__init__(self.message)

class NotFoundError(Exception):
    def __init__(self, message="Not Found"):
        self.message = message
        super().__init__(self.message)

class ForbiddenError(Exception):
    def __init__(self, message="Forbidden"):
        self.message = message
        super().__init__(self.message)

class ServerError(Exception):
    def __init__(self, message="Server Error"):
        self.message = message
        super().__init__(self.message)
