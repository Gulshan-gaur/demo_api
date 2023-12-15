# app/__init__.py
from flask import Flask
from flask_restx import Api
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app, version='1.0', title='Demo API', description='A demo API')

# Import and add namespaces
from app.resources.group_resource import group_ns
from app.resources.user_resource import user_ns
from app.resources.patient_resource import search_ns 
from app.resources.search_resource import patient_ns

api.add_namespace(group_ns)
api.add_namespace(user_ns)
api.add_namespace(patient_ns)
api.add_namespace(search_ns)
