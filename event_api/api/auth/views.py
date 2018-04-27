"""This module contains the auth endpoint routes"""

from flask import Blueprint, request, jsonify, make_response

AUTH = Blueprint('AUTH', __name__)


@AUTH.route('/api/auth/register', methods=['POST'])
def home():
    """This is the default method"""
    data = request.get_json()
    username = data['username']
    password = data['password']
    return make_response(jsonify({
        "status": "ok",
        "username": username
    }), 201)
