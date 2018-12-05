from datetime import datetime
Users = []


class User:
    user_id = 1

    def __init__(self, firstname=None, lastname=None, othernames=None, email=None, password=None, phoneNumber=None, username=None, is_admin=None):

        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.password = password
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
            password=self.password,
            phoneNumber=self.phoneNumber,
            username=self.username,
            is_admin=self.is_admin
        )

    def get_user_by_id(self, Id):
        for user in Users:
            if user.id == Id:
                return user

    @staticmethod
    def get_user_by_username(username):
        for user in Users:
            if user.username == username:
                return user

    def get_user_by_email(self, email):
        for user in Users:
            if user.email == email:
                return user
            else:
                return {"Message": "user does not exist"}, 404
