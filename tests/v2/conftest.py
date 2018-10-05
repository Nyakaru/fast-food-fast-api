from instance import create_app
import pytest
from flask_restful import Api, Resource
from app.apiv2.views.meals import Meals
from app.apiv2.views.admin import SignAdmin,LoginAdmin
from app.apiv2.views.orders import Orders
from app.apiv2.views.auth import Signup, Login
from app.apiv2.models.foodfast import drop_tables,create_tables

app = create_app('development')
api = Api(app)
api.add_resource(Meals, '/api/v2/meals')
api.add_resource(Orders, '/api/v2/orders') 
api.add_resource(Signup, '/api/v2/auth/signup') 
api.add_resource(Login, '/api/v2/auth/login') 
api.add_resource(SignAdmin, '/signadmin')
api.add_resource(LoginAdmin, '/loginadmin')      
@pytest.fixture
def create_client():
	test_app = app.test_client()
	drop_tables()
	create_tables()
	return test_app
