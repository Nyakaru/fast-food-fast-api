from flask_restful import Resource, reqparse
from flask import jsonify 
from flask_jwt_extended import create_access_token, jwt_required
from flask_bcrypt import Bcrypt

from ..models.auth import UserModel


enc = Bcrypt()

class RegisterResource(Resource):

    #get the inputs
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str,
    required = True)

    parser.add_argument('password',
    type = str,
    required = True)

    parser.add_argument('email',
    type = str,
    required = True)

    def post(self):
        data = RegisterResource.parser.parse_args()
        if UserModel(data).get_user_by_email():
            return {"message":"user already registered"}, 400
        else:
            UserModel(data).save()
            return {"message":"user registered"}, 201
        return {"message": "invalid input"}
            

class LoginResource(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('email',
    type = str,
    required = True)

    parser.add_argument('password',
    type = str,
    required = True)

    def post(self):
        data = LoginResource.parser.parse_args()
        user = UserModel(data).get_user_by_email()
        if user:
            if enc.check_password_hash(user[0].get('password'), data['password']):
                access_token = create_access_token(identity=user[0].get('user_id'))
                return {"message":"user logged in", "access_token":access_token}, 201
        return {"message":"username and password do not match"}, 400

class LogoutResource(Resource):
    def post(self):
        pass