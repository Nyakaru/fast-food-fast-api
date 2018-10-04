from flask import Flask
from flask_restful import Api
from instance.config import app_config
from app.apiv2.views.auth import Signup, Login
from app.apiv2.views.admin import SignAdmin,LoginAdmin
from app.apiv2.views.meals import Meals
from app.apiv2.views.orders import Orders, SpecificOrder, UserHistory


def create_app(config_stage):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config["development"])

    

    from app.apiv2.views.auth import auth_blueprint as auth_bp
    auth = Api(auth_bp)
    
    from app.apiv2.views.admin import admin_blueprint as admin_bp
    admin = Api(admin_bp)
    

    from app.apiv2.views.meals import meal_blueprint as meal_bp
    meal = Api(meal_bp)

    from app.apiv2.views.orders import orders_blueprint as orders_bp
    orders = Api(orders_bp)
    
    admin.add_resource(SignAdmin, '/signadmin')
    admin.add_resource(LoginAdmin, '/loginadmin')
    auth.add_resource(Signup, '/signup')
    auth.add_resource(Login, '/login')
    meal.add_resource(Meals, '/meals')
    orders.add_resource(Orders, '/orders')
    orders.add_resource(SpecificOrder, '/orders/<int:id>')
    orders.add_resource(UserHistory, '/orders/history')
    #meal.add_resource(SpecificMeal, '/meals/<int:id>')

    app.register_blueprint(auth_bp, url_prefix='/api/v2/auth')
    app.register_blueprint(meal_bp, url_prefix='/api/v2')
    app.register_blueprint(orders_bp, url_prefix='/api/v2')
    app.register_blueprint(admin_bp, url_prefix='/api/v2')
    
    return app

    