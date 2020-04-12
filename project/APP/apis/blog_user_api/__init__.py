from flask_restful import Api

from APP.apis.blog_user_api.user_resource import BlogUsersResource

user_api = Api(prefix='/blog_users')
user_api.add_resource(BlogUsersResource, '/users/')