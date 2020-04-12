from datetime import datetime

from APP.extension import db
from APP.models import BaseModel


class ArticleType(BaseModel):
    __tablename__ = 'article_type'
    type_name = db.Column(db.String(64), nullable=False)   # 类型名
    use = db.Column(db.Integer, db.ForeignKey('user.id'))


class Article(BaseModel):
    __tablename__ = 'article'
    title = db.Column(db.String(64), nullable=False)   # 标题
    describe = db.Column(db.String(256), nullable=True)  # 文章简述
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    art_type = db.Column(db.Integer, db.ForeignKey('article_type.id'))
    us = db.Column(db.Integer, db.ForeignKey('user.id'))