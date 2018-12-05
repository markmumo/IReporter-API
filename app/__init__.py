from flask import Flask
from flask_restful import Api
from app.api.v1.url import url
from instance.config import config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[config_name])

    from app.api.v1 import api_bp as api_blueprint
    api = Api(api_blueprint)

    app.register_blueprint(api_blueprint, url_prefix="/api/v1")

    url(api)

    return app
