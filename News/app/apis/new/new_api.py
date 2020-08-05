from flask import jsonify, g
from flask_restful import Resource, marshal_with, marshal, fields

from app import db
from app.apis.new import api
from app.apis.new.new_parser import types_fields, type_parser, update_type_parser, delete_type_parser, news_parser, \
    news_fields, news_detail_fields, add_news_parser
from app.model.new_model import NewsType, News
from app.utils.login_requireds import login_required


class NewsTypeApi(Resource):
    @marshal_with(types_fields)
    def get(self):
        types = NewsType.query.all()
        return types

    def post(self):

        args = type_parser.parse_args()
        typeName = args.get('typeName')

        newsType = NewsType()
        newsType.type_name = typeName
        db.session.add(newsType)
        db.session.commit()
        return marshal(newsType, types_fields)

    # 修改分类名称
    def patch(self):
        args = update_type_parser.parse_args()
        typeId = args.get('id')
        new_type_name = args.get('typeName')

        type_obj = NewsType.query.get(typeId)
        if type_obj:
            type_obj.type_name = new_type_name
            db.session.commit()
            data = {
                'status': 200,
                'msg': '修改成功',
                'type': marshal(type_obj, types_fields)
            }
        else:
            data = {
                'status': 400,
                'msg': '类型查找失败！'
            }
        return data

    # 删除分类名称
    def delete(self):
        args = delete_type_parser.parse_args()
        typeId = args.get('id')
        type_obj = NewsType.query.get(typeId)

        if type_obj:
            db.session.delete(type_obj)
            db.session.commit()
            return jsonify(status=200, msg='删除成功')
        else:
            return jsonify(status=400, msg='删除失败')


# 自定义fields类型
class AuthorName(fields.Raw):
    def format(self, value):
        return value.username


class NewsListApi(Resource):
    # 获取某个新闻分类的新闻
    def get(self):
        args = news_parser.parse_args()
        typeid = args.get('typeid')
        # newstype = NewsType.query.get(typeid)
        page = args.get('page', 1)
        pagination = News.query.filter(News.news_type_id == typeid).paginate(page=page, per_page=8)

        data = {
            'has_more': pagination.has_next,
            'data': marshal(pagination.items, news_fields),  # [news,news,news,....]
            'return_count': len(pagination.items),
            'html': 'null',
        }
        return data


class NewsDetailApi(Resource):
    @marshal_with(news_detail_fields)
    def get(self, id):
        news = News.query.get(id)
        return news


class NewsApi(Resource):

    @login_required
    def post(self):
        args = add_news_parser.parse_args()
        title = args.get('title')
        content = args.get('content')
        typeid = args.get('typeid')
        # 数据库添加
        news = News()
        news.title = title
        news.content = content
        news.desc = content[:100] + '.....'
        news.news_type_id = typeid
        news.user_id = g.user.id
        db.session.add(news)
        db.session.commit()
        data = {
            'status': 200,
            'msg': '新闻发布成功！',
            'news': marshal(news, news_detail_fields)
        }
        return data

    @login_required
    def patch(self):
        return {'msg': '新闻修改成功！'}

    @login_required
    def put(self):
        pass

    @login_required
    def delete(self):
        pass


api.add_resource(NewsTypeApi, '/types')
api.add_resource(NewsListApi, '/newslist')
api.add_resource(NewsDetailApi, '/newsdetail/<int:id>', endpoint='newsdetail')
api.add_resource(NewsApi, '/news')