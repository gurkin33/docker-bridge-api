from flask import Flask
from flask_restful import Api
from routes import RouteMaker
from config import API_PORT, API_HOST, API_DEBUG


app = Flask(__name__)
api = Api(app)

RouteMaker.run(api=api)

# if __name__ == '__main__':
#     app.run(port=API_PORT, host=API_HOST, debug=API_DEBUG)
