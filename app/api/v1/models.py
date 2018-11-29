from datetime import datetime
incidents = []
Users = []


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


class User:
    user_id = 1

    def __init__(self, firstname=None, lastname=None, othernames=None, email=None, phoneNumber=None, username=None, is_admin=None):

        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.is_admin = is_admin
        self.id = User.user_id
        User.user_id += 1

    def serialize(self):
        return dict(
            id=self.id,
            firstname=self.firstname,
            lastname=self.lastname,
            othernames=self.othernames,
            email=self.email,
            phoneNumber=self.phoneNumber,
            username=self.username,
            is_admin=self.is_admin
        )

    def get_user_by_id(self, Id):
        for user in Users:
            if user.id == Id:
                return user
            # else:

    def get_user_by_username(self, username):
        for user in Users:
            if user.username == username:
                return user

    def get_user_by_email(self, email):
        for user in Users:
            if user.email == email:
                return user
            # else:
            #     return {"Message": "user does not exist"}, 404
