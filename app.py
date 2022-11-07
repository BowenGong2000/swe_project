from flask import Flask, render_template, session, request
import pymongo
import method
from flask_restx import fields, Namespace

import db.projects as pj

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
  account_validation = True
  if account_validation:
    return render_template('homepage.html')
  return render_template('user_login.html')

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
  if request.method == 'GET':
    return render_template('add_project.html')
  else:
    project_details = (
      request.form['name'],
      request.form['member number'],
      request.form['department'],
      request.form['major'],
      request.form['school year'],
      request.form['gpa'],
      request.form['length'],
      request.form['skill'],
      request.form['information']
    )
    print(project_details)
    return render_template('add_p_success.html')

@app.route('/my_project')
def my_project():
  return render_template('my_project.html')

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