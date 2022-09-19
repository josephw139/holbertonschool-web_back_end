#!/usr/bin/env python3
""" basic auth class """


from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """ basic auth """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ base64 auth header """
        if authorization_header is None or type(
            authorization_header) is not str or not authorization_header.startswith(
                'Basic '):
                return None
        return authorization_header[6:]


    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ decode header """
        if base64_authorization_header is None or type(
            base64_authorization_header) is not str:
            return None

        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except:
            return None


    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ returns email and password """
        if decoded_base64_authorization_header is None or type(
            decoded_base64_authorization_header) is not str or ':' not in decoded_base64_authorization_header:
            return (None, None)

        tup = decoded_base64_authorization_header.split(':')
        return (tup[0], tup[1])


    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ returns USer instance based on email and password """
        if user_email is None or type(user_email) is not str or user_pwd is None or type(
            user_pwd) is not str:
            return None

        try:
            users = User.search({'email': user_email})

            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except:
            return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ retrieves User instance for request """