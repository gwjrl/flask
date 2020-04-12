from App.extension import db
from App.models import BaseModel

class Letter(BaseModel):
    letter = db.Column(db.String(1), unique=True)

class City(BaseModel):
    # 字母
    letter = db.Column(db.Integer, db.ForeignKey(Letter.id))
    c_id = db.Column(db.Integer, default=0)
    c_parentId = db.Column(db.Integer, default=0)
    c_regionName = db.Column(db.String(16))
    c_cityCode = db.Column(db.Integer, default=0)
    c_pinYin = db.Column(db.String(64))
