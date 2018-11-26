Incidents = []


class Incident():

    incident_id = 1

    def __init__(self, created_by, Type, location, status, comment, image):
        self.created_by = created_by
        self.Type = Type
        self.location = location
        self.status = status
        self.comment = comment
        self.image = image
        self.incident_id = Incident.incident_id

        self.incident_id += 1

    def serializer(self):
        return dict(
            created_by=self.created_by,
            Type=self.Type,
            location=self.location,
            status=self.status,
            comment=self.comment,
            image=self.image
        )
