from typing import Any, Dict

import requests


class Conn:

    _url: str = 'http://gateway.docker.internal:5001'
    _url_path: str = '/cmd'
    _errors: list
    _output: Any
    _access_tocken: str
    _headers: Dict[str, str] = {
        'Content-Type': 'application/json'
    }
    _auth_try: int

    def __init__(self, url: str = '', url_path: str = ''):
        if url:
            self.set_url(url)
        if url_path:
            self.set_url_path(url_path)
        self._errors = []
        self._access_tocken = ''
        self._output = None
        self._auth_try = 0

    def auth(self):
        key = ''
        with open(str(__file__).replace('conn.py', '../../pre-shared-key.txt'), 'r') as f:
            key = f.readline()
            try:
                r = requests.post(self._url + '/auth', json={"key": key}, headers=self._headers)
            except Exception:
                return False
        if r.status_code == 200:
            self._headers["Authorization"] = "Bearer {}".format(r.json()["access-token"])
            return True
        return False

    def set_url(self, url: str):
        self._url = url
        return self

    def set_url_path(self, url_path: str):
        self._url_path = url_path
        return self

    def run(self, cmd: str = ''):
        self._errors = []
        self._output = None
        if not self._headers.get("Authorization") and not self.auth():
            self._errors = ['Authentication error']
            return
        try:
            req = requests.post(self._url + self._url_path, json={"cmd": cmd}, headers=self._headers)
        except Exception:
            self._errors = ['Connection error']
            return

        if req.status_code in [401, 422] and not self._auth_try and self.auth():
            self._auth_try += 1
            self.run(cmd)
            return
        self._auth_try = 0
        if req.status_code != 200:
            self._errors = ['Connection error. Status code {}'.format(req.status_code)]
            return
        self._output = req.json()
        return

    def failed(self):
        return bool(self._errors)

    def get_errors(self):
        return self._errors

    def get_output(self):
        return self._output
