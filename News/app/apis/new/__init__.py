from flask import Blueprint
from flask_restful import Api

news_bp = Blueprint('news', __name__)
api = Api(news_bp)