from flask import Blueprint, current_app
from application import create_app

api = Blueprint('api', __name__)


@api.route("/")
def hello():
    return "Hello World!"
