
from flask import request, g
from flask_restful import abort

from App.apis.admin.model_utils import get_admin_user
from App.extension import cache

#  create a login decorator
from App.utils import ADMIN_USER


def _verify():
    token = request.args.get("token")

    if not token:
        abort(401, msg='not login')

    if not token.startswith(ADMIN_USER):
        abort(403, msg='no access')

    user_id = cache.get(token)

    if not user_id:
        abort(401, masg="please to login")

    user = get_admin_user(user_id)

    if not user:
        abort(401, masg="user not exits")
    g.user = user
    g.token = token

def login_required(fun):
    def wrapper(*args, **kwargs):
        _verify()
        return fun(*args, **kwargs)
    return wrapper

def require_permission(permission):
    def require_permission_wrapper(fun):
        def wrapper(*args, **kwargs):
            _verify()
            if not g.user.verify_permission(permission):
                abort(403, msg="you aren't the permission")
            return fun(*args, **kwargs)
        return wrapper
    return require_permission_wrapper