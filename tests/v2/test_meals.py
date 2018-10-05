import json
import unittest

from instance import create_app
from app.apiv2.models.foodfast import create_tables ,drop_tables
from .base_test import TestApp

class TestMeals(TestApp):

    
    def test_get_all_meals(self):
        token = self.get_token()
        self.client.post('/api/v2/meals',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )
        response = self.client.get(
            'api/v2/meals'
        )

        self.assertEqual(response.status_code, 200)

    def test_del_meal(self):
        token = self.get_token()
        self.client.post('/api/v2/meals',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        response = self.client.delete('/api/v2/meals/1', headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},)

        
        self.assertEqual(response.status_code, 200)

