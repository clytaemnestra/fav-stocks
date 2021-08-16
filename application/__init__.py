from flask import Flask
import os
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    from .models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from application.views import api
        app.register_blueprint(api)

    return app
