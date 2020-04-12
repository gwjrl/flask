from flask import request
from flask_restful import Resource, reqparse, abort, fields, marshal, marshal_with

from App.apis.admin.utils import login_required
from App.apis.api_constent import HTTP_CREATE_OK, HTTP_OK
from App.config import UPLOADS_DIR, FILE_PATH_PREFIX
from App.models.common.movie_model import Movie

parse = reqparse.RequestParser()
"""
 showname = db.Column(db.String(64))
    shownameen = db.Column(db.String(256))
    director = db.Column(db.String(64))
    leadingRole = db.Column(db.String(256))
    movie_type = db.Column(db.String(64))
    country = db.Column(db.String(64))
    language = db.Column(db.String(64))
    duration = db.Column(db.Integer, default=90)   # 电影时长
    screeningmodel = db.Column(db.String(32))
    openday = db.Column(db.DataTime)   # 上映日期
    background_picture = db.Column(db.String(256))
    flag = db.Column(db.Boolean, default=False)   # t推荐
    is_delete = db.Column(db.Boolean, default=False)  # 逻辑删除
    
"""
parse.add_argument("showname", required=True, help="电影名必须显示")
parse.add_argument("shownameen", required=True, help="电影英文名必须显示")
parse.add_argument("director", required=True, help="导演名必须显示")
parse.add_argument("leadingRole", required=True, help="编剧名必须显示")
parse.add_argument("movie_type", required=True, help="类型名必须显示")
parse.add_argument("country", required=True, help="国家名必须显示")
parse.add_argument("language", required=True, help="语言名必须显示")
parse.add_argument("duration", required=True, help="duration名必须显示")
parse.add_argument("screeningmodel", required=True, help="screeningmodel名必须显示")
parse.add_argument("openday", required=True, help="openday名必须显示")

# parse.add_argument("background_picture", required=True, help="图片名必须显示", location=['files'])

# 电影模板
movie_fields = {
        "showname": fields.String,
        "shownameen": fields.String,
        "director ": fields.String,
        "leadingRole": fields.String,
        "movie_type": fields.String,
        "country ": fields.String,
        "language ": fields.String,
        "duration ": fields.Integer,
        "screeningmodel": fields.String,
        "openday ": fields.DateTime,
        # "background_picture": fields.String,

}

show_movies_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(movie_fields))
}
class MoviesResource(Resource):
    @marshal_with(show_movies_fields)
    def get(self):
        movies = Movie.query.all()

        data = {
            "msg": "ok",
            "status": HTTP_OK,
            "data": movies
        }
        return data
    
    @login_required
    def post(self):
        args = parse.parse_args()
        showname = args.get("showname")
        shownameen = args.get("shownameen")
        director = args.get("director")
        leadingRole = args.get("leadingRole")
        movie_type = args.get("movie_type")
        country = args.get("country")
        language = args.get("language")
        duration = args.get("duration")
        screeningmodel = args.get("screeningmodel")
        openday = args.get("openday")
        # background_picture = args.get("background_picture")
    
        # background_picture = request.files.get("background_picture")
    
        movie = Movie()
        movie.showname = showname
        movie.shownameen = shownameen
        movie.director = director
        movie.leadingRole = leadingRole
        movie.movie_type = movie_type
        movie.country = country
        movie.language = language
        movie.duration = duration
        movie.screeningmodel = screeningmodel
        movie.openday = openday
    
        # filepath = UPLOADS_DIR + "/" + background_picture.filename
        # background_picture.save(filepath)
        #
        # movie.background_picture = FILE_PATH_PREFIX + "/" + background_picture.filename
    
        if not movie.save():
            abort(400, msg='can`t create movie')
        data = {
            "status": HTTP_CREATE_OK,
            "msg": "movie create ok",
            "data": marshal(movie, movie_fields)
        }
        return data


class MovieResource(Resource):
    def get(self, id):
        return {"msg": "get ok"}

    @login_required
    def patch(self, id ):
        return {"msg": "post ok"}
    
    # 更新
    @login_required
    def put(self, id):
        return {"msg": "post ok"}
    
    # 删除
    @login_required
    def delete(self, id):
        return {"msg": "post ok"}
