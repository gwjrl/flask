import uuid

from flask_restful import reqparse, fields, Resource, abort, marshal

from App.apis.admin.model_utils import get_admin_user
from App.apis.api_constent import USER_ACTION_REGISTER, HTTP_CREATE_OK, USER_ACTION_LOGIN, HTTP_OK
from App.config import ADMINS
from App.extension import cache
from App.models.admin.admin_user_model import AdminUser
from App.utils import generate_admin_user_token

parse_base = reqparse.RequestParser()

parse_base.add_argument("password", type=str, required=True, help="请输入密码")
parse_base.add_argument("action", type=str, required=True, help="请确认请求参数")
parse_base.add_argument("username", type=str, required=True, help="请输入用户名")


admin_user_fields = {
    "username": fields.String,
}

single_admin_user_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(admin_user_fields)
}

class AdminUsersResource(Resource):

    def post(self):
        args = parse_base.parse_args()

        password = args.get('password')

        action = args.get('action').lower()

        if action == USER_ACTION_REGISTER:
            args_register = parse_base.parse_args()
            username = args_register.get('username')

            admin_user = AdminUser()
            admin_user.username = username
            admin_user.password = password

            if username in ADMINS:
                admin_user.is_super = True

            if not admin_user.save():
                abort(400)

            data = {
                "status": HTTP_CREATE_OK,
                "msg": "用户创建成功",
                "data": admin_user
            }
            return marshal(data, single_admin_user_fields)
        elif action == USER_ACTION_LOGIN:

            args_login = parse_base.parse_args()
            username = args_login.get("username")

            user = get_admin_user(username)

            if not user:
                abort(400, msg="用户不存在")
            if not user.verify_password(password):
                abort(401, msg="用户名或密码错误")
            if user.is_delete:
               abort(401, msg="用户不存在")

            token = generate_admin_user_token()

            cache.set(token, user.id, timeout=60*60*24*7)
            data = {
                "status": HTTP_OK,
                "msg": "登陆成功",
                "data": token
            }
            return data
        else:
            abort(400, msg="请提供正确的参数")

