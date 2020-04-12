from flask import g
from flask_restful import Resource, reqparse, abort

from App.apis.movie_user.utils import login_required, require_permission
from App.models.movie_user.model_constent import VIP_USER


class MovieOrdersResource(Resource):
    @login_required
    def post(self):
        user = g.user
        return {"msg": "post_order_ok"}


class MovieOrderResource(Resource):
    @require_permission(VIP_USER)
    def put(self, order_id):
        user = g.user
        
        return {"msg": "change success"}