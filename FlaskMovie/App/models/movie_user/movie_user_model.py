from werkzeug.security import generate_password_hash, check_password_hash

from App.extension import db
from App.models import BaseModel
from App.models.movie_user.model_constent import PERMISSION_NONE, BLACK_USER


class AdminUser(BaseModel):
    username = db.Column(db.String(32), unique=True)
    _password = db.Column(db.String(256))
    phone = db.Column(db.String(32), unique=True)
    is_delete = db.Column(db.Boolean, default=False)
    permission = db.Column(db.Integer, default=PERMISSION_NONE)

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
        if (BLACK_USER & self.permission) == BLACK_USER:
            return False
        else:
            return permission & self.permission == permission