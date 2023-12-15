# app/resources/group_resource.py
from flask_restx import Namespace, Resource
from app.models import Group

group_ns = Namespace('group', description='Group operations')

@group_ns.route('/')
class GroupResource(Resource):
    def get(self):
        # Implement logic to load group names
        groups = [Group(id=1, name='Group1'), Group(id=2, name='Group2')]
        return {'groups': [{'id': group.id, 'name': group.name} for group in groups]}