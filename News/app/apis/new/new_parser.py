from flask_restful import fields, reqparse

# 标签输出
from app.apis.new.new_api import AuthorName

types_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='type_name')
}

type_parser = reqparse.RequestParser()
type_parser.add_argument('typeName', type=str, required=True, help='必须添加新闻分类名字', location='form')

# 修改的传入
update_type_parser = type_parser.copy()
update_type_parser.add_argument('id', type=int, required=True, help='必须添加要修改的分类id')

# 类型删除的传入
delete_type_parser = reqparse.RequestParser()
delete_type_parser.add_argument('id', type=int, required=True, help='必须添加要删除的分类id')

# 新闻
news_parser = reqparse.RequestParser()
news_parser.add_argument('typeid', type=int, help='必须添加新闻类型id', required=True)
news_parser.add_argument('page', type=int)

# 每条新闻的格式
news_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'desc': fields.String,
    'datetime': fields.DateTime(attribute='create_time'),
    'author': AuthorName(attribute='author'),
    'url': fields.Url('news.newsdetail', absolute=True)   # 该新闻的详情
}

# 回复的格式
reply_fields = {
    'user': AuthorName(attribute='user'),
    'content': fields.String,
    'datetime': fields.DateTime(attribute='create_time'),
    'lovenumber': fields.Integer(attribute='love_num')
}

# 评价的格式
comment_fields = {
    'user': AuthorName(attribute='user'),
    'content': fields.String,
    'datetime': fields.DateTime(attribute='create_time'),
    'lovenumber': fields.Integer(attribute='love_num'),
    'replys': fields.List(fields.Nested(reply_fields))
}

news_detail_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'datatime': fields.DateTime(attribute='create_time'),
    'author': AuthorName(attribute='author'),
    'comments': fields.List(fields.Nested(comment_fields))
}

# 回复的格式
reply_fields = {
    'user': AuthorName(attribute='user'),
    'content': fields.String,
    'datetime': fields.DateTime(attribute='create_time'),
    'lovenumber': fields.Integer(attribute='love_num')
}

# 评价的格式
comment_fields = {
    'user': AuthorName(attribute='user'),
    'content': fields.String,
    'datetime': fields.DateTime(attribute='create_time'),
    'lovenumber': fields.Integer(attribute='love_num'),
    'replys': fields.List(fields.Nested(reply_fields))
}

news_detail_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'datatime': fields.DateTime(attribute='create_time'),
    'author': AuthorName(attribute='author'),
    'comments': fields.List(fields.Nested(comment_fields))
}

# 定义新闻添加的传入
add_news_parser = reqparse.RequestParser()
add_news_parser.add_argument('title', type=str, required=True, help='必须填写新闻标题')
add_news_parser.add_argument('content', type=str, required=True, help='必须填写新闻主体内容')
add_news_parser.add_argument('typeid', type=int, required=True, help='必须填写新闻类型id')