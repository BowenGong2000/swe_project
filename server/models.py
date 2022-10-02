from flask import Flask, jsonify, request
from app import db
import uuid

class User:

    def signup(self):
        print(request.form)

        #The user form
        user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "phone": request.form.get('phone'),
      "password": request.form.get('password')
        }

        db.users.insert_one(user)

        return jsonify(user), 200