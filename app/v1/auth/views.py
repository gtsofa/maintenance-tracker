from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth

from app.v1.models import User

m_user = User()
all_users = m_user.users

# Register a user
@auth.route("/users", methods=['POST'])
def register_user():
    data = request.get_json()
    user_id = len(m_user.users) + 1 
    password_1 = data["password"]
    password_2 = data['confirm_password']
    if password_1 != password_2:
        return jsonify({"password_error": "Your password must match the confirm password"})
    user_password = generate_password_hash(data['password'])
    new_user = {
        "user_id":user_id, 
        "username":data["username"], 
        "first_name":data["first_name"], 
        "last_name":data["last_name"],
        "email":data["email"],
        "password":user_password
        }
    m_user.users[user_id] = new_user
    return jsonify({"message": "User registered successfully"}), 201

# Get all users in the system
@auth.route('/users', methods=['GET'])
def get_users():
    return jsonify(m_user.users), 200