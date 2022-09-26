#!/usr/bin/env python3
"""
auth file
"""

from multiprocessing.sharedctypes import Value
from xmlrpc.client import Boolean
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str):
        """ saves user to the db """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pwd = _hash_password(password)
            return self._db.add_user(email, pwd)

    def valid_login(self, email: str, password: str) -> Boolean:
        """ checks password """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            else:
                return False
        except:
            return False

    def create_session(self, email: str) -> str:
        """ cretes a session id """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ gets user from session_id """
        try:
            return self._db.find_user_by(session_id=session_id)
        except:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroys a session """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """ generates a reset password token """
        user = self._db.find_user_by(email=email)
        if user:
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ updates the password """
        user = self._db.find_user_by(reset_token=reset_token)
        if not user:
            raise ValueError
        pwd = _hash_password(password)
        self._db.update_user(user.id, hashed_password=pwd, reset_token=None)
        return None


def _hash_password(password: str) -> bytes:
    """ returns a hashed password """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)


def _generate_uuid() -> str:
        """ generates a uuid """
        return str(uuid4())
