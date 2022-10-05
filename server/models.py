"""
This file contain the functions and class for flask app.
"""
import uuid
from flask import jsonify, request
from app import db


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

        db.users.insert_one(user)

        return jsonify(user), 200
