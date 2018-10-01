from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import jwt_required
from ..models.menu import MenuModel

class MenuResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('menu_name',
    type = str,
    required = True)
    
    @jwt_required
    def get(self,id):
        data = {"menu_id":id}
        menu = MenuModel(data).get_by_id()
        message = "no  with {}".format(id)
        if menu:
            return jsonify(menu)
        return {"message":message}, 404
    
    @jwt_required
    def put(self,id):
        parsed_data = MenuResource.parser.parse_args()
        data_to_update={"menu_name":parsed_data['menu_name'], "menu_id":id}
        data = {"menu_id":id}
        menu = MenuModel(data).get_by_id()
        if menu:
            MenuModel(data_to_update).update_name()
            updated = MenuModel(data).get_by_id()
            return jsonify(updated)
        return {"message":"No item to update"}, 404

    @jwt_required
    def delete(self,id):
        data = {"menu_id":id}
        menu = MenuModel(data).get_by_id()
        if menu:
            try:
                MenuModel(data).delete()
                crosscheck = MenuModel(data).get_by_id()
                if crosscheck:
                    return {"message":"did not delete"}
                return {"message":" item has been deleted"}
            except Exception as e:
                print(e)

        return {"message":"item does not exist"}, 404


class MenuListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('menu_name',
    type = str,
    required = True)

    @jwt_required   
    def post(self):
        data = MenuListResource.parser.parse_args()
        if MenuModel(data).get_by_name():
            return {"message":"menu exists"}, 422
        else:
                return {"menu_name":data['menu_name']}, 201

    @jwt_required
    def get(self):
        data ={"table_name":"menus"}
        mylist = MenuModel(data).get_all()
        return jsonify(mylist)
        

 