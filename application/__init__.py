from flask import Flask
import os
from flask_migrate import Migrate
from .views import page_not_found


def create_app():
    """
    Creates factory function for application.
    https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/
    """
    application = Flask(__name__, template_folder='templates')
    application.config.from_object(os.environ['APP_SETTINGS'])
    application.register_error_handler(404, page_not_found)

    from .models import db
    db.init_app(application)
    migrate = Migrate(application, db)

    from application.views import app
    application.register_blueprint(app)

    return application

