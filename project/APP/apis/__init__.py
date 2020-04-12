# from APP.apis.admin_api import admin_api
# from APP.apis.blog_api import blog_api
from APP.apis.blog_user_api import user_api


def init_route(app):
    # admin_api.init_app(app)
    user_api.init_app(app)
    # blog_api.init_app(app)
    pass