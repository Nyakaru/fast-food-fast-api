from flask import Blueprint
from .admin import SignAdmin,LoginAdmin

admin_blueprint = Blueprint('admin', __name__)