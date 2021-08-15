from app.app import app
from flask import Blueprint

view = Blueprint('view', __name__)


@app.route("/")
def hello():
    return "Hello World!"
