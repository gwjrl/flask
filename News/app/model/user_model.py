from app import db
from app.model import BaseModel


class User(BaseModel):
    __tablename__ = 'user'

    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=True)
    icon = db.Column(db.String(255))
    # 对对多， 反向迭代
    news_list = db.relationship('News', backref='author')
    comments = db.relationship('Comment', backref='user')
    replys = db.relationship('Reply', backref='user')