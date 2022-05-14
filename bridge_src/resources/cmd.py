from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource


class Cmd(Resource):

    """"
    CMD resource is CRUD class
    """

    # @classmethod
    # @jwt_required()
    # def get(cls,):
    #     return {"CMD": "123123"}, 200

    @classmethod
    @jwt_required()
    def post(cls,):
        r = request.json
        if not r.get("cmd"):
            return {"message": "CMD required"}, 400

        return {"output": "123123"}, 200
