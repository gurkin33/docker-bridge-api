from flask_restful import Resource
import requests


class Home(Resource):

    """"
    Home resource is CRUD class
    """

    @classmethod
    def get(cls,):
        req = requests.get('http://gateway.docker.internal:5001/')
        answer = {}
        if req.status_code == 200:
            answer = req.json()
        return {"Home": answer}, 200
