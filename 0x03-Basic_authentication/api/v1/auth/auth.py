#!/usr/bin/env python3
""" auth class """


from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth Class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method """
        if path is None:
            return True
        if not path.endswith('/'):
            path = path + '/'
        if excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ header """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
