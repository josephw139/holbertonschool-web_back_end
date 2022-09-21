#!/usr/bin/env python3
""" session auth class """


from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.auth import Auth
import base64
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ session auth """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates seesion id for a user_id """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User ID based on Session ID """
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """ returns User based on cookie value """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ deletes user session / logout"""
        if request is None:
            return False
        if not self.session_cookie(request):
            return False
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        if user_id is None:
            return False
        del self.user_id_by_session_id[self.session_cookie(request)]
