from flask import Blueprint

api_blueprint = Blueprint('capstone-api', __name__)


@api_blueprint.route('/')
def get_greeting():
    greeting = "Hello World!"
    return greeting


@api_blueprint.route('/coolkids')
def be_cool():
    return "Be cool, man, be coooool! You're almost a FSND grad!"
