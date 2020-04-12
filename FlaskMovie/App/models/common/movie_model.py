from App.extension import db
from App.models import BaseModel


class Movie(BaseModel):
    __tablename__ = "movies"
    showname = db.Column(db.String(64))
    shownameen = db.Column(db.String(256))
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(256))
    movie_type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer, default=90)   # 电影时长
    screeningmodel = db.Column(db.String(32))
    openday = db.Column(db.DateTime)   # 上映日期
    flag = db.Column(db.Boolean, default=False)   # t推荐
    is_delete = db.Column(db.Boolean, default=True)  # 逻辑删除
    # background_picture = db.Column(db.String(256))