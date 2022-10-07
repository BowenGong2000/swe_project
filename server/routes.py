"""
process request form app
"""
from flask import Flask
from server.models import User

app = Flask(__name__)


@app.route('/user/signup', methods=['POST'])
def signup():
    """
    User creat account
    """
    user = User()
    return user.signup()
