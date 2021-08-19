from flask import Flask
import os
from flask_migrate import Migrate


def create_app():
    """
    Creates factory function for application.
    https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
    """
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    from .models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    from application.views import api
    app.register_blueprint(api)

    return app
