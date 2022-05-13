from flask_restful import Resource


class Home(Resource):

    """"
    Home resource is CRUD class
    """

    @classmethod
    def get(cls,):
        return {"Home": "Bridge home!"}, 200
