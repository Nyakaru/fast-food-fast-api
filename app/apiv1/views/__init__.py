from flask import Blueprint

from .orders import Orders

orders_bp = Blueprint('orders', __name__)