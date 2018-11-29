from flask import Flask
from flask_restful import Api

from app.api.v1.views import PostIncidents, Incidents, Get_incident_by_id, Get_specific_incident


def create_app():

    app = Flask(__name__)
    api = Api(app)

    """(POST) create incidents"""
    api.add_resource(PostIncidents, "/api/v1/incident")

    """GET all incidents"""
    api.add_resource(Incidents, "/api/v1/incident")

    """GET incident by id"""
    api.add_resource(Get_incident_by_id, "/api/v1/incident/<int:id>")

    """GET specific incidents """
    api.add_resource(Get_specific_incident, "/api/v1/incident/<int:id>")

    """"DELETE incident by id"""
    api.add_resource(Get_incident_by_id, "/api/v1/incident/<int:id>")

    return app
