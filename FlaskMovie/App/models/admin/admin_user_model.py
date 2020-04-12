from werkzeug.security import generate_password_hash, check_password_hash

from App.extension import db


from App.models import BaseModel
# 管理权限
PERMISSION_NONE = 0
PERMISSION_COMMON = 1

class AdminUser(BaseModel):
    __table_args__ = {'extend_existing': True}
    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    is_super = db.Column(db.Boolean, default=False)
    is_delete = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=PERMISSION_COMMON)

    # set password
    @property
    def password(self):
        raise ValueError("password can't read")

    @password.setter
    def password(self, pwd):
        self._password = generate_password_hash(pwd)

    def verify_password(self, password):
        return check_password_hash(self._password, password)

    # 检查权限
    def verify_permission(self, permission):
        return self.is_super or permission & self.permission == permission