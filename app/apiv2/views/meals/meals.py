import re
import json
from functools import wraps
import jwt
from flask_restful import Resource
from flask import request
from app.apiv2.models.models import MealItem, User

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

class Meals(Resource):
    @admin_login
    def post(self):
        ''' Method that creates a meal item '''

        data = request.get_json()
        print(data)
        
        name = data['name']
        description = data['description']
        price = data['price']
       
        if MealItem().get_by_name(name):
            return {'message': 'meal with name {name} alredy exists'}, 409

        if not re.match('^[a-zA-Z 0-9]+$', name):
            return {'message': "Enter a valid food name"}, 400

        if not re.match('^[a-zA-Z0-9 ]+$', description):
            return {'message': "Enter a valid food description"}, 400

        if type(price) != int:
            return {'message': "Invalid price"}, 400


        mealitem = MealItem(name, description, price)

        mealitem.add()
        
        return {"message": "meal item created"} ,201

    def get(self):
        '''return a list of created mealitems'''

        meal_items = MealItem().get_all_meals()
        if meal_items:
            return {
                "food_items": [meal_item.serialize() for meal_item in meal_items]
            }, 200

        return {"message": "meal item not found"}, 404


        
        















