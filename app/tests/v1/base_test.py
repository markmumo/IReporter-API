from unittest import TestCase

import json

from app import create_app


class BaseTest(TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.create_incident = {
            "created_by": "mark",
            "Type": "redflag",
            "location": "j1.1018° S, 37.0144° Euja",
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
