from flask import Flask, render_template

app = Flask(__name__)

# Routes
from server import routes


@app.route('/')
def home():
  return render_template('user_login.html')

