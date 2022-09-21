#!/usr/bin/env python3
""" Module of session_auth views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """ POST /api/v1/auth_session/login
    """
    email = request.form.get('email')
    if email is None:
        return (jsonify(({"error": "email missing"})), 400)
    password = request.form.get('password')
    if password is None:
        return (jsonify(({"error": "password missing"})), 400)

    users = User.search({'email': email})

    if len(users) == 0:
        return (jsonify(({"error": "no user found for this email"})), 404)

    for user in users:
        if not user.is_valid_password(password):
            return (jsonify({"error": "wrong password"}), 401)
        else:
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            userDict = jsonify(user.to_json())
            userDict.set_cookie(os.getenv('SESSION_NAME'), session_id)
            return userDict

@app_views.route('/auth_session/logout', methods=['DELETE'],
                     strict_slashes=False)
def logout():
    """ DELETE /api/v1/auth_session/logout
    """
    from api.v1.app import auth
    if (auth.destroy_session(request)):
        return (jsonify({}), 200)
    abort(404)
