from flask_restful import Api
from bridge_src.resources import Home, Cmd


class RouteMaker:

    _routes = [
        (Home, '/',),
        (Cmd, '/cmd',)
    ]

    @classmethod
    def run(cls, api: Api):
        for r in cls._routes:
            api.add_resource(*r)