import re
import json

from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.apiv2.models.models import MealItem, User

class Meals(Resource):
    
    def post(self):
        ''' Method that creates a meal item '''

        data = request.get_json()
        print(data)
        
        name = data['name']
        description = data['description']
        price = data['price']

        #if not (get_jwt_identity()['is_admin']):
         #   return {'message':'You cannot access this route'}, 401
       
        if MealItem().get_by_name(name):
            return {'message': 'meal with name {name} alredy exists'}, 400

        if not re.match('^[a-zA-Z 0-9]+$', name):
            return {'message': "Enter a valid food name"}, 400

        if not re.match('^[a-zA-Z0-9 ]+$', description):
            return {'message': "Enter a valid food description"}, 400

        if type(price) != int:
            return {'message': "Invalid price"}, 400


        mealitem = MealItem(name, description, price)

        mealitem.add()
        
        return {"message": "meal item created"}

    def get(self):
        
        '''return a list of created mealitems'''

        meal_items = MealItem().get_all_meals()
        
        if meal_items:
            meals = [json.dumps(i) for i in meal_items]

            return {
                "food_items": meals
            }, 200

        return {"message": "meal items not found"}

#class SpecificMeal(Resource):

 #   def delete(self, id):
        ''' Method that deletes a specific meal '''

  #      meal_item = MealItem().get_by_id(id)

   #     if meal_item:
    #        meal_item.delete(id)
     #       return {"message": "meal deleted successfully"}
      #  return {"message": "Order not found"}