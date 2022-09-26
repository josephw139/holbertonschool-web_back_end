#!/usr/bin/env python3
"""
app file
"""


import json
from urllib import response
from flask import Flask, jsonify, abort, request, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/users', methods=['POST'])
def users():
    """ registers a user """
    email = request.form.get('email')
    pwd = request.form.get('password')

    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return (jsonify({"message": "email already registered"}), 400)


@app.route('/sessions', methods=['POST'])
def login():
    """ logs in """
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not AUTH.valid_login(email, pwd):
        abort(401)

    session_id = AUTH.create_session(email=email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ logs out """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user and session_id:
        AUTH.destroy_session(session_id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """ profile """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user and session_id:
        return (jsonify({"email": user.email}), 200)
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """ reset password token """
    try:
        email = request.form.get('email')
        token = AUTH.get_reset_password_token(email)
        return (jsonify({"email": email, "reset_token": token}), 200)
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """ updates password """
    try:
        email = request.form.get('email')
        pwd = request.form.get('new_password')
        token = request.form.get('reset_token')
        AUTH.update_password(token, pwd)
        return (jsonify({"email": email,
                         "reset_token": "Password updated"}), 200)
    except Exception:
        abort(403)


@app.route('/', methods=['GET'])
def bien():
    """ returns Bienvenue message """
    return jsonify({'message': 'Bienvenue'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
