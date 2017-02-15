from flask_restful import Resource, Api, marshal_with
from flask_restful import fields
from flask_restful import reqparse

from proto import app, db
from proto.models import User

api = Api(app)

user_fields = {
    'username': fields.String,
    'email': fields.String
}


class UserListAPI(Resource):

    def __init__(self):
        self._reqparse = reqparse.RequestParser()
        self._reqparse.add_argument('username', required=True)
        self._reqparse.add_argument('email', required=True)
        super(UserListAPI, self).__init__()

    @marshal_with(user_fields)
    def get(self):
        return User.query.all()

    @marshal_with(user_fields)
    def post(self):
        args = self._reqparse.parse_args()
        user = User(args['username'], args['email'])
        db.session.add(user)
        db.session.commit()
        return user


class UserAPI(Resource):

    @marshal_with(user_fields)
    def get(self, user_id):
        return User.query.get(user_id)


api.add_resource(UserListAPI, '/users', '/users/', endpoint='users')
api.add_resource(UserAPI, '/users/<int:user_id>', endpoint='user')
