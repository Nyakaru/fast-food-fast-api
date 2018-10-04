from flask import Flask, request
from flask_restful import Resource
from app.apiv2.models.models import User, Order, MealItem


class Orders(Resource):
    #
    def post(self):
        '''post an order by the user'''

        data = request.get_json()
        name = data['name']
        qty = data["qty"]

        order = Order(name, qty)
        order.add()

        return {"message": "order placed sucessfully"}, 201


    
    def get(self):

        ''' get all orders'''
        order_items = Order().get_all_orders()
        if order_items:
            return {
                "orders": [order_item.serialize() for order_item in order_items]
            }, 200
        return {"message": "No orders found"}

class SpecificOrder(Resource):
    
    def get(self, id):
        '''get a specific order by id'''

        order = Order().get_by_id(id)

        if order:
            return {"order": order.serialize()}, 200

        return {"message": "Order not found"}, 404

    
    def put(self, id):
        ''' Method that updates a specific order '''
        
        order = Order().get_by_id(id)
        data = request.get_json()


        if data['status'].strip() == ",":
            return ({'message': 'Enter valid status input'}, 400)

        else:
            if not isinstance(data['status'], str):
                return {'message': 'Input should be a string'}
        
        if order:
            order.status = data['status']
            return {"message":order.serialize()},201
        
        return {"Message":"Order not found"},404

    
    def delete(self, id):
        ''' Method that deletes a specific order '''

        order = Order().get_by_id(id)

        if order:
            order.delete(id)
            return {"message": "order deleted successfully"}



class UserHistory(Resource):
    
    def get(self):
        ''' Method to get all orders of a particular user '''
        

        order_items = Order().get_order_history(username)

        if order_items:
            return {
                "username": username,
                "orders": [order_item.serialize() for order_item in order_items]
                
            }, 200
        return {"message": "User Not Found"}