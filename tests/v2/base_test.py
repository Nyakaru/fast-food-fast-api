import os
import json

import unittest

from instance import create_app

from app.apiv2.models.foodfast import create_tables ,drop_tables

class TestApp(unittest.TestCase):

    def setUp(self):
        """ set up test """
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            drop_tables()
            create_tables()

        self.create_user_data = {
            "username":"Useradmin",
            "email":"admin@gmail.com",
            "password": "Admin123"
        }

        self.order = {
            
	        "name":"ugali 4",
	        "qty": 2
        }
        self.meal = {
            "name":"ugali 4",
            "description": "djss",
            "price": 23
        }

        

    def signup(self):
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(self.create_user_data),
            headers={'content-type': 'application/json'}
        )
        return response

    def login(self):
        login_data = {
            "username": "Useradmin",
            "password": "Admin123"
        }
        response = self.client.post(
            "api/v2/auth/login",
            data=json.dumps(login_data),
            headers={'content-type': 'application/json'}
        )
        return response

        
    def get_token(self):
        """ function to get user token """

        self.signup()
        response = self.login()
        token = json.loads(response.data).get('token', None)
        return token

    


        

        