from app import db
from app.model import BaseModel


class NewsType(BaseModel):
    '''新闻标签类'''
    __tablename__ = 'news_type'

    type_name = db.Column(db.String(40), nullable=False)
    news_list = db.relationship('News', backref='newstype')


class News(BaseModel):
    '''新闻类'''

    __tablename__ = 'news'

    title = db.Column(db.String(128), nullable=False)
    desc = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # 多对多
    news_type_id = db.Column(db.Integer, db.ForeignKey('news_type.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    comments = db.relationship('Comments', backref='news')

    def __str__(self):
        return self.title


class Comment(BaseModel):
    __tablename__ = 'comment'
    content = db.Column(db.String(255), nullable=False)
    love_num = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))

    replys = db.relationship('Reply', backref='comment')

    def __str__(self):
        return self.content


class Reply(BaseModel):
    __tablename__ = 'reply'
    content = db.Column(db.String(255), nullable=False)
    love_num = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))

    def __str__(self):
        return self.content
