from flask import Flask
from flask_restful import Api

from app.api.v1.views import PostIncidents, GetIncidents


def create_app():

    app = Flask(__name__)
    user = Api(app)
    user.add_resource(PostIncidents, "/api/v1/incident")
    user.add_resource(GetIncidents, "/api/v1/incident")

    return app
