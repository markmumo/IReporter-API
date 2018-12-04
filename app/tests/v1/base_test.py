from unittest import TestCase
import json
from app import create_app


class BaseTest(TestCase):

    def setUp(self):
        app = create_app("testing")
        self.client = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

        self.create_incident = {
            "created_by": "mark",
            "Type": "redflag",
            "location": "j1.1018° S, 37.0144° juja",
            "status": "draft",
            "image": "corruption.png",
            "video": "corruption.webm",
            "comment": "very serious scandal"
        }

    def post_incident(self):
        response = self.client.post(
            "/api/v1/incident",
            data=json.dumps(self.create_incident),
            headers={'content-type': 'application/json'}
        )

        return response
