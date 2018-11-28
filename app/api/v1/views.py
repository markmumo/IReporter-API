# module import
from flask_restful import Resource, reqparse

from app.api.v1.models import Incident, incidents
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

        print(f"{incident.Type}")

        incidents.append(incident)

        return {"incident": "created successfully"}, 201


class Incidents(Resource):

    def get(self):
        return {"Incidents": [Incident.serializer() for Incident in incidents]}


class Get_specific_incident(Resource):

    parsing = reqparse.RequestParser()
    parsing.add_argument("created_by", type=str,
                         required=True, help="This field is required")
    parsing.add_argument("Type", type=str, required=True,
                         help="This field is required")
    parsing.add_argument("location", type=str, required=True,
                         help="This field is required")
    parsing.add_argument("status", type=str, required=True,
                         help="This field is required")
    parsing.add_argument("image", type=str, required=True,
                         help="This field is required")
    parsing.add_argument("video", type=str, required=True,
                         help="This field is required")
    parsing.add_argument("comment", type=str, required=True,
                         help="This field is required")

    """ get specific incident """

    def get(self, id):
        incident = Incident().get_incident_by_id(id)
        if not incident:
            return {"Message": "incident does not exit"}, 404
        else:
            return {"Incident": incident.serializer()}, 200


class Get_incident_by_id(Resource):
    def get(self, id):
        incident = Incident().get_incident_by_id(id)
        if not incident:
            return {"Message": "incident does not exit"}, 404
        else:
            return {"Incident": incident.serializer()}, 200
