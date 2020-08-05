from flask import request, g
from flask_restful import abort

from app.ext import cache
from app.model.user_model import User


def check_user():
    auth = request.headers.get('Authorization')
    if not auth:
        abort(401, msg='请先登录')
    mobile = cache.get(auth)
    if not mobile:
        abort(401, msg='无效令牌')
    user = User.query.filter(User.phone == mobile).first()
    if not user:
        abort(401, msg='此用户已被管理员删除')
    g.user = user


def login_required(func):
    def wrapper(*args, **kwargs):
        check_user()
        return func(*args, **kwargs)
    return wrapper
