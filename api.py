from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from config import DBConfig
from models import setup_db
from routes import (api_blueprint, bad_request, page_not_found,
                    unprocessable, internal_server_error, handle_auth_error)


def create_api():
    api = Flask(__name__)
    
    api.register_blueprint(api_blueprint, url_prefix='/api')
    api.register_error_handler(400, bad_request)
    api.register_error_handler(401, handle_auth_error)
    api.register_error_handler(404, page_not_found)
    api.register_error_handler(422, unprocessable)
    api.register_error_handler(500, internal_server_error)

    api.config.from_object(DBConfig)
    db = setup_db(api)
    CORS(api)
    migrate = Migrate(api, db)

    return api, migrate


api, migrate = create_api()


if __name__ == '__main__':
    api.run()
