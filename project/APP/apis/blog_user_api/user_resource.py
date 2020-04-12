


from flask_restful import Resource, reqparse


from APP.extension import db

parse_base = reqparse.RequestParser()
parse_base.add_argument("password")



class BlogUsersResource(Resource):

    def post(self):
        pass

    def user_register(self):
        pass
