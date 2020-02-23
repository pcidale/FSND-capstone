from flask import Blueprint, jsonify
from auth import AuthError, requires_auth

api_blueprint = Blueprint('capstone-api', __name__)


@api_blueprint.route('/')
def get_greeting():
    greeting = "Hello World!"
    return greeting


@api_blueprint.route('/coolkids')
@requires_auth('get:coolkids')
def be_cool():
    return "Be cool, man, be coooool! You're almost a FSND grad!"


# Error Handling
@api_blueprint.errorhandler(400)
def bad_request(error):
    """
        Handler for bad request
        :param error:
        :return: status code and json with error message
        """
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400


@api_blueprint.errorhandler(404)
def page_not_found(error):
    """
        Handler for resources not found
        :param error:
        :return: status code and json with error message
        """
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@api_blueprint.errorhandler(422)
def unprocessable(error):
    """
    Handler for unprocessable errors
    :param error:
    :return: status code and json with error message
    """
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@api_blueprint.errorhandler(500)
def internal_server_error(error):
    """
    Handler for internal errors
    :param error:
    :return: status code and json with error message
    """
    return jsonify(
        {
            'success': False,
            'message': 'internal error',
            'error': 500
        }
    ), 500


@api_blueprint.errorhandler(AuthError)
def handle_auth_error(exception):
    """
    Authentication error handler for scoped endpoints
    :param exception: AuthError instance
    :return: response: status code and the error description
    """
    response = jsonify(exception.error)
    response.status_code = exception.status_code
    return response
