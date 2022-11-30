from flask import Response, jsonify


def make_error(message: str, status: int = 400) -> Response:
    response = jsonify(message=message)
    response.status_code = status
    return response
