from flask import jsonify


def bad_request(message, status_code=400):
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = status_code
    return response
