import unittest
import json

from instance import create_app
# from flask import jsonify, current_app
from app.apiv2.models.foodfast import create_tables ,drop_tables
from  .base_test import TestApp

class TestUser(TestApp):

    def setUp(self):
        """ set up test """

        self.app = create_app("development")
        self.client = self.app.test_client()

        self.create_user_data = {
            "username":"Kinadmin",
            "email":"kin@gmail.com",
            "password": "kinara"
        }
            
        with self.app.app_context():
            drop_tables()
            create_tables()
            

    def test_invalid_email(self):
        create_user_data = {
                "username":"kinara",
                "email":"nyakaru.com",
                "password": "password"}
        
        response = self.client.post(
            "api/v2/auth/signup",
            data=json.dumps(create_user_data),
            headers={'content-type': 'application/json'}
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.data)["message"], "Please enter a valid email")

    


    
