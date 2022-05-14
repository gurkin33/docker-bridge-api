import subprocess

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
        timeout = 20
        if r.get("timeout"):
            timeout = r.get("cmd")
        if not r.get("cmd") or not isinstance(r.get("cmd"), str):
            return {"message": "CMD required"}, 400
        # std_out, std_err = ('', '')
        try:
            process = subprocess.Popen(
                r["cmd"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
            process.wait(timeout=timeout)
            std_out, std_err = process.communicate()

        except Exception as e:
            return {"message": "Cannot execute", "exception": str(e)}, 400

        return {"out": str(std_out), "err": str(std_err)}, 200
