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

    """ GET specific incident """

    def get(self, id):
        incident = Incident().get_incident_by_id(id)
        if not incident:
            return {"Message": "incident does not exit"}, 404
        else:
            return {"Incident": incident.serializer()}, 200

    """ GET incident by id """


class Get_incident_by_id(Resource):

    def get(self, id):
        incident = Incident().get_incident_by_id(id)
        if not incident:
            return {"Message": "incident does not exit"}, 404
        else:
            return {"Incident": incident.serializer()}, 200

    """" DELETE specific incident """

    def delete(self, id):
        delete_incident = Incident().get_incident_by_id(id)
        if not delete_incident:
            return {"message": "incident does not exist"}, 404
        else:
            incidents.remove(delete_incident)
            return {"Message": "Incident deleted successfully"}, 200

    """ (PATCH) update specific incident """

    def patch(self, id):

        data = Get_specific_incident.parsing.parse_args()

        created_by = data['created_by']
        Type = data['Type']
        location = data['location']
        status = data['status']
        image = data['image']
        video = data['video']
        comment = data['comment']

        specific_incident = Incident().get_incident_by_id(id)

        if not specific_incident:
            return {"message": "This incident does not exist"}, 404
        else:
            specific_incident.created_by = created_by
            specific_incident.Type = Type
            specific_incident.location = location
            specific_incident.status = status
            specific_incident.image = image
            specific_incident.video = video
            specific_incident.comment = comment

            return {"Incident": specific_incident.serializer()}, 200
