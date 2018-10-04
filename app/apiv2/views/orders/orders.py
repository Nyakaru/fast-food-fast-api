from flask import Flask, request
from flask_restful import Resource
from app.apiv2.models.models import User, Order, MealItem
from functools import wraps
import jwt

def auth_login(func):
    @wraps(func)
    def decorate_function(*args,**kwargs):
        if 'LOGIN-KEY' in request.headers:
            token_key = request.headers['LOGIN-KEY']
            print token_key

            try:
                values = jwt.decode(token_key,'verysecret')
                print values
                

            except:
                return 'Invalid Token error'  
        else:
            return 'No token passed'
        return func(*args, **kwargs)

    return decorate_function

def admin_login(func):
    @wraps(func)
    def decorate_function(*args,**kwargs):
        if 'ADMIN-KEY' in request.headers:
            token_key = request.headers['ADMIN-KEY']
            print token_key

            try:
                values = jwt.decode(token_key,'verysecret')
                print values
                

            except:
                return 'Invalid Token error'  
        else:
            return 'No token passed'
        return func(*args, **kwargs)

    return decorate_function

class Orders(Resource):
    @auth_login
    def post(self):
        '''post an order by the user'''

        data = request.get_json()
        name = data['name']
        qty = data["qty"]

        order = Order(name, qty)
        order.add()

        return {"message": "order placed sucessfully"}, 201


    @admin_login
    def get(self):

        ''' get all orders'''
        order_items = Order().get_all_orders()
        if order_items:
            return {
                "orders": [order_item.serialize() for order_item in order_items]
            }, 200
        return {"message": "No orders found"}

class SpecificOrder(Resource):
    @admin_login
    def get(self, id):
        '''get a specific order by id'''

        order = Order().get_by_id(id)

        if order:
            return {"order": order.serialize()}, 200

        return {"message": "Order not found"}, 404

    @admin_login
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

    @admin_login
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