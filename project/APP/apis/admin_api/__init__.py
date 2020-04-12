from flask_restful import Api

from APP.apis.admin_api.admin_resource import AdminResource

admin_api = Api(prefix='/admins')
admin_api.add_resource(AdminResource)