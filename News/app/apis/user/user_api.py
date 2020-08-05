
import random
import uuid

from flask import jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.apis.user import api
from app.apis.user.user_parser import sms_parser, lr_parser, reset_parser, update_parser, password_login_parser
from app.ext import cache, session
from app.model.user_model import User
from app.utils.send_message import send_duanxin


# 发送手机验证码类视图
class SendMessageApi(Resource):
    def psot(self):
        args = sms_parser.parse_args()
        mobile = args.get('mobile')
        ret, code = send_duanxin(mobile)

        if ret is not None:
            if ret["code"] == 200:
                cache.set(mobile, code, timeout=1800)
                return jsonify(code=200, msg='短信发送成功')
        else:
            return jsonify(code=400, msg='短信发送失败')


class LoginAndRegisterApi(Resource):
    def post(self):
        args = lr_parser.parse_args()
        phone = args.get('mobile')
        code = args.get('code')
        cache_code = cache.get(phone)
        if cache_code and code == cache_code:
            user = User.query.filter(User.phone == phone).first()

            if not user:
                user = User()
                user.phone = phone

                s = ''
                for i in range(13):
                    ran = random.randint(0,9)
                    s += str(ran)
                user.username = '用户' + s

                db.session.add(user)
                db.session.commit()

            token = str(uuid.uuid4()).replace('-', '') + str(random.randint(100, 999))
            cache.set(token, phone)
            return jsonify(status=200, msg='登录成功', token=token)
        else:
            return jsonify(status=400, errmsg='验证码错误')


class ForgetPasswordApi(Resource):

    def get(self):
        s = 'QWERTYUIOPLKJHGFDSAZXCVBNMzxcvbnmlkjhgfdsaqwertyuiop1234567890'
        code = ''
        for i in range(4):
            ran = random.choice(s)
            code += ran

        session['code'] = code
        return jsonify(code=code)


class ResetPasswordApi(Resource):
    def get(self):
        args = reset_parser.parse_args()
        phone = args.get('mobile')
        imageCode = args.get('imageCode')
        code = session.get('code')

        if code and imageCode.lower() == code.lower():
            user = User.query.filter(User.phone == phone).first()
            if user:
                ret, smscode = send_duanxin(phone)
                if ret is not None:
                    if ret['code'] == 200:
                        cache.set(phone, smscode, timeout=180)
                        return jsonify(status=200, msg='短信发送成功')
                else:
                    return jsonify(status=400, msg='短信发送失败')
            else:
                return jsonify(status=400, msg='此用户未注册')
        else:
            return jsonify(status=400, msg='验证码有误')


class UserApi(Resource):
    def post(self):
        args = password_login_parser.parse_args()
        mobile = args.get('mobile')
        password = args.get('password')
        # 判断用户
        user = User.query.filter(User.phone == mobile).first()
        if user:
            if check_password_hash(user.password, password):
                # 说明用户是登录成功的 dfjkdj-hdfjhsd34-sdjf83748-3847fnmm
                token = str(uuid.uuid4()).replace('-', '') + str(random.randint(100, 999))
                print('token:', token)
                # 存储用户的登录信息
                cache.set(token, mobile)
                return {'status': 200, 'msg': '用户登录成功', 'token': token}

        return {'status': 400, 'msg': '账户名或者密码有误！'}

    def put(self):
        args = update_parser.parse_args()
        code = args.get('code')
        mobile = args.get('mobile')
        cache_code = cache.get(mobile)
        # 判断验证码是否输入正确
        if cache_code and cache_code == code:
            user = User.query.filter(User.phone == mobile).first()
            password = args.get('password')
            repassword = args.get('repassword')
            # 判断密码是否输入一致
            if password == repassword:
                user.password = generate_password_hash(password)
                db.session.commit()
                return {'status': 200, 'msg': '设置密码成功'}
            else:
                return {'status': 400, 'msg': '两次密码不一致'}
        else:
            return {'status': 400, 'msg': '验证码有误'}


api.add_resource(SendMessageApi, '/sms')
api.add_resource(LoginAndRegisterApi, '/codelogin')
api.add_resource(ForgetPasswordApi, '/forget')
api.add_resource(ResetPasswordApi, '/reset')
api.add_resource(UserApi, '/user')