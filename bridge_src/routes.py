from flask_restful import Api
from bridge_src.resources import Cmd, Auth


class RouteMaker:

    _routes = [
        (Cmd, '/cmd',),
        (Auth, '/auth',)
    ]

    @classmethod
    def run(cls, api: Api):
        for r in cls._routes:
            api.add_resource(*r)
