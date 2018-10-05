from flask_restful import Resource
from flask import  Flask,jsonify,request,Response,json
from app.apiv1.models.models import orders, Order


orders = []

class Orderss(Resource):
    """
    GET/ all orders placed
    POST/ a new order
    """
    
    def get(self):
        """Return a list of all orders posted"""
        if len(orders) == 0:
            return {'messsage': 'Empty orders list'}, 200
        return {'orders': orders}, 200

    def post(self):
        """Posts a specific order"""
        order_data = {}
        data = request.get_json()
        order_data['name'] = data['name']
        order_data['price'] = data['price']
        order_data['description'] = data['description']
        order_data['id'] = len(orders) + 1    
        orders.append(order_data)
        return {"message":"Order created",'orders': order_data}, 201
        if name in orders:
            return {'message': 'Order already exists'}

class OneOrder(Resource):
    """
    GET/ a specific order
    PUT/ edit a specific order
    DELETE/ delete a specific order 
    """
    def get(self, id):
        order = [order for order in orders if order['id'] == id]
        if order:
            return {'order': order[0]}, 200
        else:
            return {'message':'Error,you order was not found'}, 200
    
    def put(self, id):
        order = [order for order in orders if order['id'] == id]
        if order:
            data = request.get_json()
            order[0]['name'] = data['name']
            order[0]['price'] = data['price']
            order[0]['description'] = data['description']
               
            # orders.append(order_data)
            return {'order': order[0]}, 200
        else:
            return {'message':'Error ,Invalid order object'}, 200
    
    def delete(self, id):
        order = [order for order in orders if order['id'] == id]
        if order:
            del orders[0]
            return {'orders': orders}, 204
        else:
            return {'message': 'Error ,Invalid order object'}, 204
class AcceptedOrders(Resource):

    def get(self):
        acceptedOrders = []
        for order in orders:
            if order.status == "accepted":
                acceptedOrders.append(order)
                return {"message":[order.serialize() for order in acceptedOrders]},200

        return {"message":"unfortunately there are no accepted orders"},200


class DeclineOrder(Resource):

    def put(self,id):

        order = Order().get_specific(id)
        if order:
            if order.status != "pending" and order.status == "declined":
                return {"message":"order already {}".format(order.status)}
            
            order.status = "declined"
            return {"message":"yeah,the order declined successfully"}
        
        return {"message":"Damn!Your order was not found"}

class DeclinedOrders(Resource):
    
    def get(self):

        declinedorders = []
        for order in orders:
            if order.status == "rejected":
                declinedorders.append(order)
        
        
        return {"rejected orders":[order.serialize() for order in declinedorders]}
        

class PendingOrders(Resource):
    def get(self):
        pendingorders = []
        for order in orders:
            if order.status == "waiting":
                pendingorders.append(order)
        return {"waiting orders":[order.serialize() for order in pendingorders]}


class CompleteOrder(Resource):
    def put(self,id):
        order = Order().get_specific(id)
        if order:
            if order.status != "approved":
                return {"message":"The order is already {}".format(order.status)}
            if order.status == "approved":
                order.status = "delivered"
                return {"message":"Order has beeen completed and will be delivered"}
        return {"message":"order not found"}
class CompletedOrders(Resource):
    def get(self):
        completedorders = []
        for order in orders:
            if order.status == "delivered":
                completedorders.append(order)
        return {"delivered orders":[order.serialize() for order in completedorders]}

