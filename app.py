from flask import Flask, render_template, session, request
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

@app.route('/homepage', methods = ['GET', 'POST'])
def homepage():
  return render_template('homepage.html')

@app.route('/homepage_search', methods=['GET', 'POST'])
def homepage_search():
  name = session['name']
  email = session['phone']
  phone = session['email']
  key_word = request.form['key_word']

  # if key_word != None:
    # execute something that returns everything related to the keyword
    

  # unfinished

  return render_template('/homepage.html')

if __name__ == '__main__':    
    app.run(debug=True)