from flask import Flask
from flask_restful import Api
from app.apiv1.orders.views import Orders, SpecificOrder, AcceptedOrders,DeclineOrder,DeclinedOrders,PendingOrders,CompleteOrder,CompletedOrders
from instance.config import app_config


def create_app(config_name='development'):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config["development"])
	app.config.from_pyfile('config.py')
	from .apiv1.orders import orders_bp as orders_blueprint
	api = Api(orders_blueprint)
	app.register_blueprint(orders_blueprint, url_prefix='/api/v1')
	api.add_resource(Orders, '/orders')
	api.add_resource(SpecificOrder, '/orders/<int:id>')
	api.add_resource(AcceptedOrders,'/orders/approved')
	api.add_resource(DeclineOrder,'/orders/decline/<int:id>')
	api.add_resource(DeclinedOrders,'/orders/declined')
	api.add_resource(PendingOrders,'/orders/pending')
	api.add_resource(CompleteOrder,'/orders/completeorder/<int:id>')
	api.add_resource(CompletedOrders,'/orders/completed')

	return app
	
