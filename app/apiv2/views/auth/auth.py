import re
import os

from flask_restful import Resource
from flask import request
from werkzeug.security import check_password_hash
import jwt
from app.apiv2.models.models import User

class Signup(Resource):
    def post(self):
        ''' Add a new user '''
        data = request.get_json()

        username = data['username']
        email = data["email"]
        password = data['password']

        if not re.match('^[a-zA-Z0-9]{6,20}$', username):
            return {'message':'Please enter a valid username'}, 400

        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            return {'message': 'Invalid email'}, 400

        if not re.match("^[a-zA-Z0-9$!#]{8,20}$", password):
            return {'message':'Enter a valid password'}, 400
        
        if User().get_user_by_username(username):
            return {'message': 'username already in use'}, 400
       


        user = User(username, email, password)

        user.add()

        return {'message': 'Account created successfully'}, 201

class Login(Resource):
    def post(self):
        ''' Existing user can login '''
        data = request.get_json()

        username = data['username']
        password = data['password']

        #user = User(username=username,password=password)
        user = User().get_user_by_username(username)
        user_dict = user.serialize()
        if not user:
            return {'message': 'user not found'}, 404
        result = check_password_hash(user_dict["password"], password)
        if not result:
            return {'message': 'Wrong password'}, 400
        else:
            token = jwt.encode({'data' : user_dict },'verysecret',algorithm = 'HS256')#create_access_token(user.serialize())
            return {
                'token': token,
                'message': 'You were successfully logged in {}'.format(username)
            }, 200


