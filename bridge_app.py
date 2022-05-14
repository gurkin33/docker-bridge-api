import string
from random import choice, randint

from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api
from bridge_src import RouteMaker


app = Flask(__name__)

app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400  # 1 day
app.config["JWT_SECRET_KEY"] = ''.join(
    choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(randint(32, 64)))

# Pre-shared key for auth between docker app and bridge
with open('pre-shared-key.txt', 'w') as f:
    f.write(''.join(
        choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(randint(64, 128))))

api = Api(app)

jwt = JWTManager(app)


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'message': 'Token has expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'message': 'Wrong token'
    }), 401


@jwt.unauthorized_loader
def unauthorised_callback(error):
    return jsonify({
        'message': 'Authorization header required',
    }), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_callback(error):
    return jsonify({
        'message': 'Token is not fresh'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'message': 'Token has been revoked'
    }), 401


RouteMaker.run(api=api)
