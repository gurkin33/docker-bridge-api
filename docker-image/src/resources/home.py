from flask_restful import Resource
import requests

from src.bridge_conn import Conn


class Home(Resource):

    """"
    Home resource is CRUD class
    """

    @classmethod
    def get(cls,):
        output = ''
        conn = Conn()
        conn.run('ls -a')
        if conn.failed():
            return {"errors": conn.get_errors()}, 400

        return {"output": conn.get_output().get('out'), "error": conn.get_output().get('err')}, 200
