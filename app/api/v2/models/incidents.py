from datetime import datetime
incidents = []


class Incident:

    incident_id = 1

    def __init__(self, created_by=None, Type=None, location=None, status=None, image=None, video=None, comment=None):

        self.created_on = datetime.now().replace(second=0, microsecond=0)
        self.created_by = created_by  # represents the user who created this record
        self.Type = Type  # [red-flag, intervention]
        self.location = location  # Lat Long coordinates

        # [draft, under investigation, resolved, rejected]
        self.status = status
        self.image = image
        self.video = video
        self.comment = comment
        self.id = Incident.incident_id

        Incident.incident_id += 1

    def serializer(self):
        return dict(
            id=self.id,
            created_on=str(self.created_on),
            created_by=self.created_by,
            Type=self.Type,
            location=self.location,
            status=self.status,
            image=self.image,
            video=self.video,
            comment=self.comment
        )

    def get_incident_by_id(self, id):
        for incident in incidents:
            if incident.id == id:
                return incident
