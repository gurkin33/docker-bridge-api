from typing import Any

import requests


class Conn:

    _url: str = 'http://gateway.docker.internal:5001'
    _url_path: str = '/cmd'
    _errors: list
    _output: Any

    def __init__(self, url: str = '', url_path: str = ''):
        if url:
            self.set_url(url)
        if url_path:
            self.set_url_path(url_path)
        self._errors = []
        self._output = None

    def set_url(self, url: str):
        self._url = url
        return self

    def set_url_path(self, url_path: str):
        self._url_path = url_path
        return self

    def run(self, cmd: str = ''):
        self._errors = []
        self._output = None
        try:
            req = requests.get(self._url + self._url_path)
        except Exception:
            self._errors = ['Connection error']
            return
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
