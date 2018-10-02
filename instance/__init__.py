from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from app.apiv1.orders.views import Orders, SpecificOrder,AcceptedOrders,DeclineOrder,CompleteOrder
from instance.config import app_config
from app.apiv2.views.auth import Signup, Login
from app.apiv2.views.meals import Meals

jwt = JWTManager()

def create_app(config_stage):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_stage])

    jwt.init_app(app)

    from app.apiv2.views.auth import auth_blueprint as auth_bp
    auth = Api(auth_bp)
    app.register_blueprint(auth_bp, url_prefix='/api/v2/auth')

    from app.apiv2.views.meals import meal_blueprint as meal_bp
    meal = Api(meal_bp)
    app.register_blueprint(meal_bp, url_prefix='/api/v2')


    from app.apiv1.orders import orders_bp as orders_blueprint
    api = Api(orders_blueprint)
    app.register_blueprint(orders_blueprint, url_prefix='/api/v1')

    auth.add_resource(Signup, '/signup')
    auth.add_resource(Login, '/login')
    api.add_resource(Orders, '/orders')
    meal.add_resource(Meals, '/meals')
    api.add_resource(SpecificOrder, '/orders/<int:id>')
    api.add_resource(AcceptedOrders,'/orders/accept/<int:id>')
    api.add_resource(DeclineOrder,'/orders/decline/<int:id>')
    api.add_resource(CompleteOrder,'/orders/completeorder/<int:id>')
    
    app = Flask(__name__)
    return app

    