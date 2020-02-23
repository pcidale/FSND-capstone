import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DBConfig:
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Auth0Config:
    domain = os.getenv('AUTH0_DOMAIN')
    domain = os.getenv('AUTH0_ALGORITHMS')
    domain = os.getenv('AUTH0_AUDIENCE')
