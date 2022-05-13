from flask_restful import Resource
import requests

from src.bridge_conn import Conn


class Home(Resource):

    """"
    Home resource is CRUD class
    """

    @classmethod
    def get(cls,):
        conn = Conn()
        conn.run()
        if conn.failed():
            return {"errors": conn.get_errors()}

        return {"Home": conn.get_output()}, 200
