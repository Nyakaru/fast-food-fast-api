from flask import Blueprint

from app.apiv2.views.auth import Signup, Login

from app.apiv2.views.meals import Meals

from app.apiv2.views.orders import Orders, SpecificOrder, UserHistory

from app.apiv2.views.admin import SignAdmin,LoginAdmin

admin_blueprint = Blueprint('admin', __name__)
auth_blueprint = Blueprint('auth', __name__)
meal_blueprint = Blueprint('meals', __name__)
orders_blueprint = Blueprint('orders', __name__)
