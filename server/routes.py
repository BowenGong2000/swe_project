from flask import Flask
from app import app
from server.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
  user = User()
  return user.signup()
