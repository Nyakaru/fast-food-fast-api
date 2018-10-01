from flask_restful import Resource, reqparse
from flask import jsonify
import simplejson as json
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.orders import OrderModel

class CustomersOrdersListResource(Resource):
    parser = reqparse.RequestParser()
    
    parser.add_argument('meal_id',
    type = int,
    required = True)

    parser.add_argument('quantity',
    type = int,
    required = True)
    
    @jwt_required   
    def post(self):
        parsed_data = CustomersOrdersListResource.parser.parse_args()
        if OrderModel(parsed_data).get_meal_name() == None:
            return {"message":"meal item does not exists"}, 422
        else:
            current_user = get_jwt_identity()
            # user_data = {'user_name':user_name}
            user_id = {'user_id':current_user}
            token_id = current_user
            user_name = OrderModel(user_id).get_user_name()
            meal_name = OrderModel(parsed_data).get_meal_name()
            total = OrderModel(parsed_data).calculate_price()
            data = {'meal_id':parsed_data['meal_id'], 'user_id':token_id, 'quantity':parsed_data['quantity'],
                'total':total
            }
            OrderModel(data).save()
            data_to_return = {'meal_name':meal_name['meal_name'], 'ordered_by':user_name['user_name'], 'total':total}
            return (data_to_return) 

    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        data = {"user_id":user_id}
        orders = OrderModel(data).get_user_orders()
        return jsonify(orders)

class AdminOrdersListResource(Resource):
    @jwt_required
    def get(self):
        data ={"table_name":"orders"}
        mylist = OrderModel(data).get_all()
        return jsonify(mylist)

class OrdersResource(Resource):

    #get a specific order 
    def get(self,id):
        data = {"order_id":id}
        meal = OrderModel(data).get_by_id()
        message = "no order with {}".format(id)
        if meal:
            return jsonify(meal)
        return {"message":message}, 404
       

class AdminOrdersResource(Resource):
    def put(self, id):
        pass

    def get(self, id):
        pass
    
    