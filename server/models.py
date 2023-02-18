"""
This file contain the details for the user login system.
"""
from flask import jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
import uuid

import db.user as usr


class User:
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    """
    info of user
    """
    def signup(self):
        '''
        user registration
        '''
        print(request.form)

        '''
        type of user should be 1 for normal user 2 for manager account
        '''
        user_email = request.form.get('email')
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "phone": request.form.get('phone'),
            "password": request.form.get('password')
        }
        """
        Encrypt the password
        """
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        """
        Check for same email address
        """
        if usr.user_exists(user_email):
            return jsonify({"error": "Email address already existed"}), 400

        if usr.add_user(user_email, user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):

        user_email = request.form.get('email')

        user_exist = usr.user_exists(user_email)

        """ Verify if input password match with db password """

        pwd_db = usr.get_user_password(user_email)
        pwd_ipt = request.form.get('password')
        check = pbkdf2_sha256.verify(pwd_ipt, pwd_db)

        if user_exist and check:
            user = usr.get_user_details(user_email)
            return self.start_session(user)
        return jsonify({"error": "Invalid login credentials"}), 401
