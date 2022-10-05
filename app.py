from flask import Flask, render_template
import pymongo
import method

app = Flask(__name__)

client = pymongo.MongoClient('mongodb+srv://tracyzhu0608:1234@cluster0.8pa03kh.mongodb.net/?retryWrites=true&w=majority', 27017)
db = client.user_login_system

# Routes
from server import routes

@app.route('/')
def home():
  return render_template('user_login.html')

# @app.route('/')
# def home():
#   return render_template('homepage.html')

if __name__ == '__main__':    
    app.run(debug=True)