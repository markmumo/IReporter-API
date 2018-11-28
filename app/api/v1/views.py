# module import
from flask_restful import Resource, reqparse

from app.api.v1.models import Incident, Incidents
from utils.validators import Validate


class PostIncidents(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("created_by", type=str, required=True)
    parser.add_argument("Type", type=str, required=True)
    parser.add_argument("location", type=str, required=True)
    parser.add_argument("status", type=str, required=True)
    parser.add_argument("image", type=str, required=True)
    parser.add_argument("video", type=str, required=True)
    parser.add_argument("comment", type=str, required=True)

    def post(self):
        data = PostIncidents.parser.parse_args()

        created_by = data["created_by"]
        Type = data["Type"]
        location = data["location"]
        status = data["status"]
        image = data["image"]
        video = data["video"]
        comment = data["comment"]

        validating = Validate()

        if not validating.is_string(created_by):
            return {"message": "must be a string"}, 400

        if not validating.is_string(Type):
            return {"type": "must be a string"}, 400

        incident = Incident(created_by, Type, location,
                            status, comment, image, video)

        Incidents.append(incident)

        return {"incident": "created successfully"}, 201

        print(f"{incident.Type}")
