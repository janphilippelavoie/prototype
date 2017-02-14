from flask_restful import Resource, Api, marshal_with, marshal
from flask_restful import fields

from proto.models import User
from proto import app

api = Api(app)

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String
}


class UserListAPI(Resource):

    def get(self):
        return {'users': marshal(User.query.all(), user_fields)}


class UserAPI(Resource):

    @marshal_with(user_fields)
    def get(self, user_id):
        return User.query.get(user_id)

    def post(self):
        pass


api.add_resource(UserListAPI, '/users', endpoint='users')
api.add_resource(UserAPI, '/users/<int:user_id>', endpoint='user')
