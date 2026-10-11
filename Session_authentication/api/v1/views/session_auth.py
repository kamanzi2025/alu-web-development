#!/usr/bin/env python3
"""Module of the Session authentication views: login and logout routes."""
from os import getenv
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'],
                 strict_slashes=False)
def session_login() -> str:
    """POST /api/v1/auth_session/login logs a user in with a session."""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        users = []
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response
    return jsonify({"error": "wrong password"}), 401


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout() -> str:
    """DELETE /api/v1/auth_session/logout destroys the user's session."""
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
