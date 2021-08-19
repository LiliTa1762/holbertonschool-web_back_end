#!/usr/bin/env python3
"""Basic Flask app"""


from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """first route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """end-point to register a user"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email,
                        "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Log in method"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    if session_id is not None:
        resp = make_response(jsonify({"email": email, "message": "logged in"}))
        resp.set_cookie("session", session_id)
        return resp


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Log out function"""
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    AUTH.destroy_session(user_id)
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
