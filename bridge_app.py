from flask import Flask
from flask_restful import Api
from bridge_src import RouteMaker


app = Flask(__name__)
api = Api(app)

RouteMaker.run(api=api)
