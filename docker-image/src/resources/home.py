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
        conn.run('ll')
        if conn.failed():
            return {"errors": conn.get_errors()}
        if isinstance(conn.get_output(), dict) and conn.get_output().get('output'):
            output = conn.get_output().get('output')
        return {"output": output}, 200
