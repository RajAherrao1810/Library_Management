import os
from flask import Blueprint, request, jsonify
from database import execute_query, fetch_one

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')

    member = fetch_one("SELECT * FROM members WHERE email = ?", (email,))
    if not member:
        return jsonify({'error': 'Invalid email'}), 400

    token = os.urandom(16).hex()
    execute_query("INSERT INTO tokens (member_id, token) VALUES (?, ?)", (member['id'], token))
    return jsonify({'token': token})

@auth.route('/validate', methods=['POST'])
def validate():
    data = request.json
    token = data.get('token')

    token_entry = fetch_one("SELECT * FROM tokens WHERE token = ?", (token,))
    if token_entry:
        return jsonify({'message': 'Token is valid'})
    return jsonify({'error': 'Invalid token'}), 401
