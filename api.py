from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from config import DBConfig
from models import setup_db
from route import api_blueprint


def create_api():
    api = Flask(__name__)
    api.register_blueprint(api_blueprint, prefix='/api')
    api.config.from_object(DBConfig)
    setup_db(app)
    CORS(app)
    migrate = Migrate(api)

    return app, migrate


if __name__ == '__main__':
    app, migrate = create_api()
    app.run()
