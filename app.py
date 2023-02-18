import os
from flask import Flask, url_for, render_template, session, request, redirect, send_file, make_response, flash
from flask_restx import Resource
from functools import wraps
import datetime
import difflib
import heapq

from user_login import User
import db.projects as pj
import method as mth


app = Flask(__name__)
app.secret_key = 'hskfakgkajgalg' #random key


#export data from database
#todo give top matches
def homepage_form(key_word = None):
  temp_project_dict = pj.get_projects_dict()
  project_lst = []
  project_dict = {}
  for key in temp_project_dict:
    #todo add time limit functions like (datetime.datetime.today() - temp_project_dict[key]['post_date']).days < 90
    if temp_project_dict[key]['if_approve']:
      project_lst.append(temp_project_dict[key])
      project_dict[key] = temp_project_dict[key]
  if not key_word or not temp_project_dict:
    return project_lst
  return rank_for_relation_to_key_work(project_dict, key_word.lower())

#transfer dict to list store with content as plain text and keys
def dict_to_lst_of_string(project_dict):
  ret_lst = []
  for key in project_dict:
    temp = ''
    for sub_key in project_dict[key]:
      if sub_key == 'account':
        temp = temp + project_dict[key]["account"]['email'] + " " + project_dict[key]["account"]['name']
      elif isinstance(project_dict[key][sub_key], str):
        temp += " " + project_dict[key][sub_key]
    ret_lst.append([key, temp.lower()])
  return ret_lst


#return ranked project based on relation to key_word
def rank_for_relation_to_key_work(project_dict, key_word):
  unrank_lst = dict_to_lst_of_string(project_dict)
  heap = []
  ret_project_lst = []
  for ele in unrank_lst:
    score = difflib.SequenceMatcher(None, key_word, ele[1]).ratio()
    heapq.heappush(heap, (-score, ele[0]))
  while len(heap) > 0:
    curr_proj = project_dict[heapq.heappop(heap)[1]]
    ret_project_lst.append(curr_proj)
  return ret_project_lst
  

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

@app.route('/user/signup', methods=['POST'])
def signup():
    """
    User create account
    """
    user = User()
    return user.signup()


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login()


@app.route('/')
def home():
  return render_template('user_login.html')

@app.route('/homepage', methods = ['GET', 'POST'])
@login_required
def homepage():
  if session["user"]['email'].split('_')[0] == "Manager":
    return render_template('manager_homepage.html')
  project_lst = homepage_form()
  return render_template('homepage.html', project_lst = project_lst)

@app.route('/homepage_local', methods=['GET', 'POST'])
def homepage_local():
  #todo return homepage base on account passed in through url
  project_lst = homepage_form()
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
      'post_date': datetime.datetime.today().strftime("%m-%d-%Y"),
      "description": request.form["description"],
      "if_approve": True
      #todo need request("FS")
    }

  if pj.check_if_exist(request.form['name']):
    flash("Error: Project name already existed.")
    return render_template('add_project.html')

  else:
    pj.add_project(proj_name, project_details)
    flash("Thank you for sharing your project with us.")
    return render_template('my_project.html')
  

@app.route('/single_post/<project>', methods=['GET', 'POST'])
def single_post(project):
  project = pj.get_project_details(project)
  return render_template('post.html', project = project)

@app.route('/my_project')
def my_project():
  return render_template('my_project.html')

@app.route('/my_application')
def my_application():
  return render_template('my_application.html')

@app.route('/homepage_search', methods=['GET', 'POST'])
def homepage_search():
  key_word = request.form['key_word']
  project_lst = homepage_form(key_word)
  return render_template('homepage.html', project_lst = project_lst)


@app.route('/images/<file_name>', methods = ['GET'])
def get_file(file_name):
  file_name = os.path.join("templates/images",file_name)
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

@app.route('/contact_us', methods = ['GET'])
def contact_us():
  return render_template("contact.html")

if __name__ == '__main__':    
    app.run(debug=True)