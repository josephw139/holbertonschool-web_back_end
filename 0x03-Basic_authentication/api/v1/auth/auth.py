#!/usr/bin/env python3
""" auth class """


from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth Class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method """
        if not path.endswith('/'):
            path = path + '/'
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """ header """
        if request is None:
            return None
        if request.has_key('Authorization'):
            return request['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
