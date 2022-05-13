from flask_restful import Api
from src.resources import User, Home


class RouteMaker:

    _routes = [
        (Home, '/',),
        (User, '/user', '/user/<int:user_id>')
    ]

    @classmethod
    def run(cls, api: Api):
        for r in cls._routes:
            api.add_resource(*r)
