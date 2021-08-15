from flask import Flask, request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

from . import models
models.db.init_app(app)
migrate = Migrate(app, models.db)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
