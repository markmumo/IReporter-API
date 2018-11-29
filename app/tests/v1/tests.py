import json

from .base_test import BaseTest


class TestIncident(BaseTest):

    def test_post_incident(self):

        response = self.post_incident()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)[
                         "incident"], "created successfully")

        """Test get incident"""

    def test_get_incidents(self):
        response = self.client.get("/api/v1/incident")
        self.assertEqual(response.status_code, 200)

        """Test get incident by id"""

    def test_get_incident_by_id(self):

        self.post_incident()

        response = self.client.get(
            "/api/v1/incident/3",
            headers={'content-type': 'application/json'}
        )

        self.assertEqual(response.status_code, 200)

        """Test to delete an incident"""

    def test_delete_incident_by_id(self):

        self.post_incident()
        response = self.client.delete(
            "/api/v1/incident/1",
            headers={'content-type': 'application/json'}
        )

        self.assertEqual(response.status_code, 200)

        """Test to  update specific incident"""

    def test_patch(self):

        res = self.post_incident()
        response = self.client.patch(
            "/api/v1/incident/3",
            data=json.dumps(self.create_incident),
            headers={
                'content-type': 'application/json'
            }
        )

        self.assertEqual(response.status_code, 200)
