"""
This file contain the functions and class for flask app.
"""
from flask import jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
import pymongo
import uuid

#Database
client = pymongo.MongoClient('mongodb+srv://tracyzhu0608:1234@cluster0.8pa03kh.mongodb.net/?retryWrites=true&w=majority', 27017)
db = client.user_login_system

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
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        """
        Encrypt the password
        """
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        """
        Check for same email address
        """
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already existed"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):

        user = db.users.find_one({
            "email": request.form.get('email')
        })

        pwd_db = user['password']
        pwd_ipt = request.form.get('password')
        check = pbkdf2_sha256.verify(pwd_ipt, pwd_db)

        if user and check:
            return self.start_session(user)
        return jsonify({"error": "Invalid login credentials"}), 401
