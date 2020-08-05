from flask import Blueprint
from flask_restful import Api

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

