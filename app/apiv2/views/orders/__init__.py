from flask import Blueprint

from .orders import Orders, SpecificOrder, UserHistory

orders_blueprint = Blueprint('orders', __name__)

