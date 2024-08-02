"""
API Wrapper
---------------------

"""

# imports
import certifi as cfi
from json import dumps
from kivy.network.urlrequest import UrlRequest
from kivymd.app import MDApp
from kivy.storage.jsonstore import JsonStore


class API:
    _HEADERS = None

    def __init__(self, headers=None):
        # self._HEADERS = headers
        self._HEADERS = headers if headers else {"Content-Type": "application/json"}


    def post_request(self,
                     url,
                     instance,
                     on_success_method=None,
                     on_error_method=None,
                     on_failure_method=None,
                     method: str = 'POST',
                     payload: dict = None
                     ):
        """
        :param
            url: str = request url
            instance: methd = model instance (self)
            on_success_method: methd = custom success method for callback
            on_error_method: methd = custom error method for callback
            on_failure_method: methd = custom failure method for callback
            payload: dict
            headers: dict = custom headers
        """

        req = UrlRequest(
            url,
            req_body=dumps(payload),
            method=method,
            req_headers=self._HEADERS,
            on_success=instance.on_success if on_success_method is None else on_success_method,
            on_error=instance.on_error if on_error_method is None else on_error_method,
            on_failure=instance.on_failure if on_failure_method is None else on_failure_method,
            ca_file=cfi.where(),
            verify=True
        )
        return req
