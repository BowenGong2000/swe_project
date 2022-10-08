"""
This file contain the functions and class for flask app.
"""
import uuid
from flask import jsonify, request
from app import db
from passlib.hash import pbkdf2_sha256


class User:
    """
    info of user
    """
    def signup(self):
        '''
        user registration
        '''
        print(request.form)

        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "phone": request.form.get('phone'),
            "password": request.form.get('password')
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])
        
        # Check for same email address
        if db.users.find_one({ "email": user['email'] }):
            return jsonify({ "error": "Email address already existed" }), 400

        if db.users.insert_one(user):
            return jsonify(user), 200

        return jsonify({ "error": "Signup failed" }), 400
