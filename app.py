from flask import Flask, render_template, session, request, redirect, send_file, make_response
import pymongo
import method as mth
from flask_restx import Resource
from functools import wraps
import db.projects as pj
import os

app = Flask(__name__)
app.secret_key = 'hskfakgkajgalg' #random key

#Database
client = pymongo.MongoClient('mongodb+srv://tracyzhu0608:1234@cluster0.8pa03kh.mongodb.net/?retryWrites=true&w=majority', 27017)
db = client.user_login_system

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  return wrap

# Routes
from server import routes

@app.route('/')
def home():
  return render_template('user_login.html')

@app.route('/homepage', methods = ['GET', 'POST'])
@login_required
def homepage():
  return render_template('homepage.html')
  #account_validation = 1 user, 2 manager, 0 invalid
  email = request.form['email']
  password = request.form['password']
  #todo password encode (i think it is done in 'model.py')
  #todo account validation
  account_type = mth.account_validation(email, password)
  
  if account_type == 1:
    return render_template('homepage.html')
  elif account_type == 2:
    #todo function that inplement info for manager count into dict_manager
    dict_manager = mth.manager_info(email)
    return render_template('manager_homepage.html', info = dict_manager)
  return render_template('user_login.html')

@app.route('/homepage_local', methods=['GET', 'POST'])
def homepage_local():
  #todo return homepage base on account passed in through url
  return render_template('homepage.html')

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
  if request.method == 'GET':
    return render_template('add_project.html')
  else:
    project_details = (
      request.form['name'],
      request.form['member number'],
      request.form['depart'],
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

@app.route('/user_homepage')
def user_homepage():
  return render_template('user_homepage.html')

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


@app.route('/images/<file_name>', methods = ['GET'])
def get_file(file_name):
  file_name = os.path.join("templates\images",file_name)
  #print(file_name)
  return send_file(file_name)

if __name__ == '__main__':    
    app.run(debug=True)