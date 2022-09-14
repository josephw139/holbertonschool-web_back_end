#!/usr/bin/env python3
"""
Main file
"""

from xmlrpc.client import Boolean
import bcrypt


def hash_password(password):
    """ returns a salted, hasged password """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def is_valid(hashed_password: bytes, password: str) -> Boolean:
    """ check if password is valid """
    checkPass = password.encode('utf-8')
    result = bcrypt.checkpw(checkPass, hashed_password)
    return result
