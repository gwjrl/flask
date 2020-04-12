from werkzeug.security import generate_password_hash, check_password_hash

from APP.extension import db
from APP.models import BaseModel


class User(BaseModel):
    # 表名
    __tablename__ = 'user'
    # 字段
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    _password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(255), unique=True)
    header_img = db.Column(db.String(255), nullable=True)  # 头像
    phone = db.Column(db.String(255), unique=True)
    is_delete = db.Column(db.Boolean, default=False)  # 逻辑删除用户

    #设置密码
    @property
    def password(self):
        raise AttributeError("你没有有权限")

    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)

    def verify_password(self, password):
        # 检查密码
        return check_password_hash(self.password, password)
