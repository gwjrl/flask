from datetime import datetime

from app import db


class BaseModel(db.Model):
    '''
    定义抽象基类
    '''
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.now)



    def delete(self):
        db.session.delete(self)
        db.session.commit()