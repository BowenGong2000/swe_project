"""
process request form app
"""
from server.models import User
from app import app


@app.route('/user/signup', methods=['POST'])
def signup():
    """
    User creat account
    """
    user = User()
    return user.signup()
