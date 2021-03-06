from flask import Flask
from flask_restful import Resource, reqparse

from app.api.v1.models.incidents import Incident, incidents
from app.api.v1.models.users import User, Users
from utils.validators import Validate


class Sign_in(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    def post(self):
        data = Sign_in.parser.parse_args()
        username = data['username']
        password = data['password']
        user = User.get_user_by_username(username)
        if user and user.password == password:
            return {"Message": f"{user.username} created successfully"}, 201

        return {"Message": "Username not found"}, 404


class Sign_up(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('firstname', type=str, required=True)
    parser.add_argument('lastname', type=str, required=True)
    parser.add_argument('othernames', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('phoneNumber', type=str, required=True)
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('is_admin', type=bool, required=True)

    def post(self):
        data = Sign_up.parser.parse_args()
        firstname = data['firstname']
        lastname = data['lastname']
        othernames = data['othernames']
        email = data['email']
        password = data['password']
        phoneNumber = data['phoneNumber']
        username = data['username']
        is_admin = data['is_admin']

        if not Validate.validate_username(username):
            return {"Message": "username can only contain alphanumeric characters only and a minimum of 4 characters"}, 400
        if not Validate.validate_phone_number(phoneNumber):
            return {"Message": "please put valid phone number"}, 400

        if not Validate.validate_input_strings(firstname):
            return {"Message": "Please enter valid firstname"}, 400
        if not Validate.validate_input_strings(lastname):
            return {"Message": "Please enter valid lastname"}, 400
        if not Validate.validate_input_strings(othernames):
            return {"Message": "Please enter valid names"}, 400
        if not Validate.validate_password(password):
            return {"Message": "Password must be at least 8 characters"}, 400
        if User().get_user_by_email(email):
            return {"Message":"email adress already taken"}, 400
        if User().get_user_by_username(username):
            return {"Message": f"{username} already taken, please try another"}, 400

        user = User(firstname, lastname, othernames, email, password,
                    phoneNumber, username, bool(is_admin))
        Users.append(user)
        return {"Message": f"{user.username} created successfully"}, 201


class All_users(Resource):
    def get(self):
        return {"Users": [user.serialize() for user in Users]}


class Get_users_by_email(Resource):
    def get(self, email):

        user = User().get_user_by_email(email)
        if user:
            return {"User": user.serialize()}


class Get_user_by_id(Resource):
    def get(self, id):
        user = User().get_user_by_id(id)
        if not user:
            return{"User does not exist"}
        else:
            return {"User": user.serialize()}
