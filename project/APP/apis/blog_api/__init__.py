from flask_restful import Api

from APP.apis.blog_api.blog_resource import BlogResource

blog_api = Api(prefix='/blogs')
blog_api.add_resource(BlogResource)