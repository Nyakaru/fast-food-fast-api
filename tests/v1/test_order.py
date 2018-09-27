
import unittest

import json

from app import create_app

from unittest import TestCase

from flask_restful import Resource

from app.apiv1.views.orders import SpecificOrder, Orders, AcceptedOrders, DeclineOrder, DeclinedOrders, PendingOrders, CompleteOrder, CompletedOrders




class TestApi(unittest.TestCase):

    

    def setUp(self):

        self.app = create_app("testing")

        self.client = self.app.test_client()

        self.app_context = self.app.app_context()

        self.new_order = {"name": "Kill", "price": 200200, "description": "tasty"}



    def test_get_orders(self):
        """
            Tests if the route gets a list of all orders
    """
        response = self.client.get('/api/v1/orders' ,content_type='application/json')
        self.assertEqual(response.status_code, 200)



    def test_post_orders(self):

        response = self.client.post('/api/v1/orders', data = json.dumps(self.new_order), content_type='application/json')

        self.assertEqual(response.status_code, 201)

    
    def test_one_order(self):
        """Returns a 200 status code if an order is fetched"""
        response = self.client.get('/api/v1/orders/1' ,content_type='application/json')

        self.assertEqual(response.status_code, 200)


    def test_put_order(self):

        response = self.client.put('/api/v1/orders/1', data = json.dumps(self.new_order), content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def test_delete_order(self):
        response = self.client.delete('/api/v1/orders/1', content_type='application/json')
        self.assertEqual(response.status_code, 204)



    def test_get_completed_orders(self):
        response = self.client.get(
            'api/v1/orders/completed',
            headers = {"content-type":"application/json"}
        )
        self.assertEqual(response.status_code,200)


    def test_get_pending_orders(self):
        response = self.client.get(
            'api/v1/orders/pending',
            headers = {"content-type":"application/json"}
        )
        self.assertEqual(response.status_code,200)

    def test_complete_order(self):
        response = self.client.put(
            'api/v1/orders/completeorder/1',
            headers = {"content-type":"application/json"}
        )
        self.assertEqual(response.status_code,200)
        

    def test_decline_order(self):
        response = self.client.put(
            "api/v1/orders/decline/1",
            headers = {"content-type":"application/json"}
        )

        self.assertEqual(response.status_code,200)

    def test_declined_orders(self):
        response = self.client.get(
            "api/v1/orders/declined",
        headers = {"content-type":"application/json"}
        )
        self.assertEqual(response.status_code,200)

    def test_get_approved_orders(self):
        response = self.client.get(
            "api/v1/orders/approved",
            headers = {"content-type":"application/json"}
        )

        self.assertEqual(response.status_code,200)



if __name__ == '__main__':

    unittest.main()