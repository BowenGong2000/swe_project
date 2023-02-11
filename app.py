from flask import Flask, url_for, render_template, session, request, redirect, send_file, make_response
import pymongo
import method as mth
from flask_restx import Resource
from functools import wraps
import db.projects as pj
import os
import datetime


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

#export data from database
#todo give top matches
def homepage_form(info = None):
  temp_project_lst = pj.get_projects_dict()
  project_lst = []
  for key in temp_project_lst:
    if (datetime.datetime.today() - temp_project_lst[key]['post_date']).days < 90:
      temp_project_lst[key]['post_date'] = temp_project_lst[key]['post_date'].strftime("%m-%d-%Y")
      project_lst.append(temp_project_lst[key])
  return project_lst

# Routes
from server import routes


@app.route('/')
def home():
  return render_template('user_login.html')

@app.route('/homepage', methods = ['GET', 'POST'])
@login_required
def homepage():
  if session["user"]['email'].split('_')[0] == "Manager":
    return render_template('manager_homepage.html')
  project_lst = homepage_form(info = None)
  return render_template('homepage.html', project_lst = project_lst)

@app.route('/homepage_local', methods=['GET', 'POST'])
def homepage_local():
  #todo return homepage base on account passed in through url
  project_lst = homepage_form(info = None)
  return render_template('homepage.html', project_lst = project_lst)

@app.route('/add_project', methods=['GET', 'POST'])
def add_project():
  if request.method == 'GET':
    return render_template('add_project.html')
  else:
    proj_name  = request.form['name']
    project_details = {
      'name': request.form['name'],
      'account': session['user'],
      'num_members': request.form['member number'],
      'department_name': request.form['depart'],
      'major_requirements': request.form['major'],
      'school_year': request.form['school year'],
      'GPA' :request.form['gpa'],
      'project_duration': request.form['length'],
      'skill requirements': request.form['skill'],
      'post_date': datetime.datetime.today()
      #todo need request("FS")
    }
    pj.add_project(proj_name, project_details)
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


@app.route('/images/<file_name>', methods = ['GET'])
def get_file(file_name):
  file_name = os.path.join("templates\images",file_name)
  return send_file(file_name)


@app.route("/account", methods=['GET', 'POST'])
def account():
    image_file = url_for('static', filename='images/' + 'steven.jpg')
    return render_template('account.html', title='Account', image_file=image_file)

@app.route("/manager_homepage", methods=['GET', 'POST'])
def manager_homepage():
  return render_template("manager_homepage.html")

@app.route('/about_us', methods = ['GET'])
def about_us():
  return render_template("about_us.html")

if __name__ == '__main__':    
    app.run(debug=True)