from flask_restful import reqparse, inputs, fields

sms_parser = reqparse.RequestParser()

sms_parser.add_argument('mobile', type=inputs.regex(r'^1[356789]\d{9}$'), help='手机格式错误', required=True)

# 登录注册
lr_parser = sms_parser.copy()
lr_parser.add_argument('code', type=inputs.regex(r'^\d{4}$'), help='必须输入四位验证码', requried=True)

user_fields = {
    'id': fields.Integer,
    'username': fields.String
}

# 申请重置密码
reset_parser = sms_parser.copy()
reset_parser.add_argument('imageCode', type=inputs.regex(r'^[a-zA-Z0-9]{4}$'), help='必须输入正确格式的验证码')

# 更新密码以及登陆前的操作
update_parser = lr_parser.copy()
update_parser.add_argument('password'
                           , type=inputs.regex(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,10}$')
                           , help='必须包含大小写字母和数字的组合，不能使用特殊字符'
                           , location='form')
update_parser.add_argument('repassword'
                           , type=inputs.regex(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,10}$')
                           , help='必须包含大小写字母和数字的组合，不能使用特殊字符'
                           , location='form')

# 登录设置需要前端传入的内容
password_login_parser = sms_parser.copy()
password_login_parser.add_argument('password', type=str, help='必须输入密码', required=True, location='form')
