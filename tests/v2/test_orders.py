import json
import unittest

from instance import create_app
from app.apiv2.models.foodfast import create_tables ,drop_tables
from .base_test import TestApp


class TestOrders(TestApp):
    def setUp(self):
        """ set up test """
        self.app = create_app("testing")
        self.client = self.app.test_client()
        with self.app.app_context():
            drop_tables()
            create_tables()
        self.order = {
            
            "name":"ugali 4",
            "qty": 2
        }   
    
    def test_post_order(self):
        token = self.get_token()
        self.client.post('/api/v2/orders', 
            headers = {"content-type":"application/json"},
            data = json.dumps(self.meal)
        )
        
        print(response.data)
        self.assertEqual(response.status_code, 201)

    
    def test_get_all_orders(self):
        token = self.get_token()
        self.client.post('/api/v2/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        self.client.post('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.order)
        )

        response = self.client.get('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
        )


        print(response.data)
        self.assertEqual(response.status_code, 200)

    

    def test_delete_order(self):
        token = self.get_token()
        self.client.post('/api/v2/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        self.client.post('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.order)
        )

        response = self.client.delete('/api/v2/users/orders/1',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            )
        
        self.assertEqual(response.status_code, 200)

    def test_get_user_order_history(self):
        token = self.get_token()
        self.client.post('/api/v2/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.meal)
        )

        self.client.post('/api/v2/users/orders',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
            data=json.dumps(self.order)
        )

        response = self.client.get('api/v2/users/history',
            headers = {"content-type":"application/json", "Authorization": "Bearer {}".format(token)},
        
        )

        self.assertEqual(response.status_code, 200)




