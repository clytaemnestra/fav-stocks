from flask import Blueprint
# from application import create_app

api = Blueprint('api', __name__)


@api.route("/")
def hello():
    return "Hello World!"
