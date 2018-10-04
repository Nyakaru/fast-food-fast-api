import re
import os

from flask_restful import Resource
from flask import request
from werkzeug.security import check_password_hash
import jwt
from app.apiv2.models.models import Admin


class SignAdmin(Resource):
    def post(self):
        ''' Register an admin '''
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

        admin = Admin(username, email, password)

        admin.add()

        return {'message': 'Account created successfully'}, 201

class LoginAdmin(Resource):
    def post(self):
        ''' Existing admin can login '''
        data = request.get_json()

        username = data['username']
        password = data['password']

        #user = User(username=username,password=password)
        admin = Admin().get_admin_by_username(username)
        admin_dict = admin.serialize()
        if not admin:
            return {'message': 'user not found'}, 404
        result = check_password_hash(admin_dict["password"], password)
        if not result:
            return {'message': 'Wrong password'}, 400
        else:
            token = jwt.encode({'data' : admin_dict },'verysecret',algorithm = 'HS256')#create_access_token(user.serialize())
            return {
                'token': token,
                'message': 'You were successfully logged in {}'.format(username)
            }, 200
