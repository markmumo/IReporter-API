from flask import Flask
from flask_restful import Api

from app.api.v1.views import All_users, Get_incident_by_id, Get_user_by_id, \
    Get_users_by_email, Incidents, PostIncidents, Sign_in, Sign_up
from instance.config import app_config


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

    """Delete incident id"""

    api.add_resource(Get_incident_by_id, "/api/v1/incident/<int:id>")

    """SignUp"""
    api.add_resource(Sign_up, '/api/v1/Sign_up')

    """SignIn"""
    api.add_resource(Sign_in, '/api/v1/Sign_in')

    """GET all Users"""
    api.add_resource(All_users, '/api/v1/users')
    api.add_resource(Get_user_by_id, '/api/v1/users/<int:id>')
    api.add_resource(Get_users_by_email, '/api/v1/users/<string:email>')

    return app
