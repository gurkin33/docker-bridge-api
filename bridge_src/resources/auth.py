import datetime

from flask import request, jsonify
from flask_jwt_extended import create_access_token, set_access_cookies
from flask_restful import Resource


class Auth(Resource):

    """"
    Auth resource
    """

    @classmethod
    def post(cls,):
        req = request.json

        if not req.get('key'):
            return {"message": 'Authentication failed'}, 401

        with open(str(__file__).replace('auth.py', '../../pre-shared-key.txt'), 'r') as f:
            if f.readline() == req.get('key'):
                access_token = create_access_token(
                    identity={"created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                )
                resp = jsonify({'access-token': access_token})

                set_access_cookies(resp, access_token)

                return resp

        return {"message": 'Authentication failed'}, 401
