from flask import Blueprint

from .orders import PostOrder, SpecificOrder, UserHistory

orders_blueprint = Blueprint('orders', __name__)

