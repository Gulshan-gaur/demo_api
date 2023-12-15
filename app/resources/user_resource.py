# app/resources/user_resource.py
from flask_restx import Namespace, Resource
from app.models import User

user_ns = Namespace('user', description='User operations')

@user_ns.route('/<int:group_id>')
class UserResource(Resource):
    def get(self, group_id):
        # Implement logic to load users for a given group_id
        users = [User(id=1, name='User1'), User(id=2, name='User2')]
        return {'users': [{'id': user.id, 'name': user.name} for user in users]}
