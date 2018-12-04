from flask import Flask
from flask_restful import Api
from instance.config import app_config
from app.api.v1.views import PostIncidents, Incidents, Get_incident_by_id


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    api = Api(app)

    """(POST) create incidents"""
    api.add_resource(PostIncidents, "/api/v1/incident")

    """GET all incidents"""
    api.add_resource(Incidents, "/api/v1/incident")

    """GET incident by id"""
    api.add_resource(Get_incident_by_id, "/api/v1/incident/<int:id>")

    return app
