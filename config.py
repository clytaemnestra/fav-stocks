import os
from tempfile import mkdtemp
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    CSFR_ENABLED = True
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'].replace("://", "ql://", 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True