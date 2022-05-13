from flask_restful import Resource


class Cmd(Resource):

    """"
    CMD resource is CRUD class
    """

    @classmethod
    def get(cls,):
        return {"CMD": "123123"}, 200

    @classmethod
    def post(cls,):
        return {"CMD": "123123"}, 200
