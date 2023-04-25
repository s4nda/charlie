class APIException(Exception):
    status_code = None

class ValidationError(APIException):
    status_code = 400

