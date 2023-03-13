"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask, request, send_file
from flask_restx import Resource, Api, fields, Namespace, reqparse
from passlib.hash import pbkdf2_sha256
from werkzeug.datastructures import FileStorage

import db.data_type as dtyp
import db.projects as pj
import db.user as usr
import db.application as apl

import werkzeug.exceptions as wz
from io import BytesIO
import mimetypes


app = Flask(__name__)
api = Api(app)

DATA_NS = 'data'
PROJECTS_NS = 'projects'
USERS_NS = 'users'
APPLICATION_NS = 'application'

data_types = Namespace(DATA_NS, 'Data Types')
api.add_namespace(data_types)
projects = Namespace(PROJECTS_NS, 'Projects')
api.add_namespace(projects)
users = Namespace(USERS_NS, 'Users')
api.add_namespace(users)
applications = Namespace(APPLICATION_NS, 'Applications')
api.add_namespace(applications)

LIST = 'list'
DICT = 'dict'
HELLO = '/hello'
MESSAGE = 'message'
DETAILS = 'details'
ADD = 'add'
CHANGE = 'change'
DELETE = 'delete'
FILE = 'file'
USER = 'user'
PROJECT = 'project'
GET = 'get'

MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'

DATA_DICT = f'/{DICT}'
DATA_DICT_W_NS = f'{DATA_NS}/{DICT}'
DATA_DICT_NM = f'{DATA_NS}_dict'
DATA_LIST = f'/{LIST}'
DATA_LIST_NM = f'{DATA_NS}_list'
DATA_LIST_W_NS = f'{DATA_NS}/{LIST}'
DATA_DETAILS = f'/{DETAILS}'
DATA_DETAILS_W_NS = f'{DATA_NS}/{DETAILS}'

PROJECT_DICT = f'/{DICT}'
PROJECT_DICT_W_NS = f'{PROJECTS_NS}/{DICT}'
PROJECT_DETAILS = f'/{DETAILS}'
PROJECT_DETAILS_W_NS = f'{PROJECTS_NS}/{DETAILS}'
PROJECT_LIST = f'/{LIST}'
PROJECT_LIST_NM = f'{PROJECTS_NS}_list'
PROJECT_LIST_W_NS = f'{PROJECTS_NS}/{LIST}'
PROJECT_ADD = f'/{ADD}'
PROJECT_CHANGE_FIELD = f'/{CHANGE}'
PROJECT_DELETE = f'/{DELETE}'
PROJECT_ADD_FILE = f'/{FILE}/{ADD}'
PROJECT_DELETE_FILE = f'/{FILE}/{DELETE}'
PROJECT_CHANGE_FILE = f'/{FILE}/{CHANGE}'
PROJECT_GET_FILE = f'/{FILE}/{GET}'

USER_DICT = f'/{DICT}'
USER_DICT_NM = f'{USERS_NS}_dict'
USER_DICT_W_NS = f'{USERS_NS}/{DICT}'
USER_DETAILS = f'/{DETAILS}'
USER_DETAILS_W_NS = f'{USERS_NS}/{DETAILS}'
USER_LIST = f'/{LIST}'
USER_LIST_NM = f'{USERS_NS}_list'
USER_LIST_W_NS = f'{USERS_NS}/{LIST}'
USER_ADD = f'/{ADD}'
USER_LOGIN = '/login'
USER_SIGNUP = '/signup'
USER_UPDATE = '/update'
USER_DELETE = f'/{DELETE}'

APPLICATION_DICT = f'/{DICT}'
APPLICATION_DICT_W_NS = f'{APPLICATION_NS}/{DICT}'
APPLICATION_DETAILS = f'/{DETAILS}'
APPLICATION_DETAILS_W_NS = f'{APPLICATION_NS}/{DETAILS}'
APPLICATION_USER = f'/{USER}'
APPLICATION_USER_W_NS = f'{APPLICATION_NS}/{USER}'
APPLICATION_DELETE = f'/{DELETE}'
APPLICATION_ADD = f'/{ADD}'
APPLICATION_PROJECT = f'/{PROJECT}'
APPLICATION_PROJECT_W_NS = f'{APPLICATION_NS}/{PROJECT}'


project_fields = api.model('NewProject', {
    pj.ACCOUNT: fields.String,
    pj.NAME: fields.String,
    pj.DEPARTMENT: fields.String,
    pj.MAJOR: fields.String,
    pj.SCHOOL_YEAR: fields.String,
    pj.NUM_MEMBERS: fields.Integer,
    pj.GPA: fields.Float,
    pj.LENGTH: fields.String,
    pj.SKILL: fields.String,
    pj.DESCRIP: fields.String,
    pj.POST_DATE: fields.String,
    pj.APPROVE: fields.Boolean,
})

user_fields = api.model('NewUser', {
    usr.EMAIL: fields.String,
    usr.NAME: fields.String,
    usr.PHONE: fields.String,
    usr.PW: fields.String,
})

login_user_fields = api.model('LoginUser', {
    usr.EMAIL: fields.String,
    usr.PW: fields.String,
})

application_fields = api.model('NewApplication', {
    apl.NAME: fields.String,
    apl.APPLICANT_NAME: fields.String,
    apl.APPLICANT_EMAIL: fields.String,
    apl.PROJECT: fields.String,
    apl.APP_DATE: fields.String,
    apl.RESUME: fields.String,
    apl.TRANSCRIPT: fields.String,
    apl.APP_STATUS: fields.String,
})


@api.route('/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {MESSAGE: 'hello world'}


@api.route(MAIN_MENU)
class MainMenu(Resource):
    """
    This will deliver our main menu.
    """
    def get(self):
        """
        Gets the main menu.
        """
        return {'Title': MAIN_MENU_NM,
                'Default': 1,
                'Choices': {
                    '1': {'url': f'/{PROJECT_DICT_W_NS}',
                          'method': 'get',
                          'text': 'List Current Projects.'},
                    '2': {'url': f'/{USER_DICT_W_NS}',
                          'method': 'get',
                          'text': 'List USERS.'},
                    'X': {'text': 'Exit'},
                }}


@data_types.route(DATA_LIST)
class DataList(Resource):
    """
    This will get a list of data types
    """
    def get(self):
        """
        Return a list of data types
        """
        return {DATA_LIST_NM: dtyp.get_data_types()}


@data_types.route(f'{DATA_DETAILS}/<data_type>')
class DataTypeDetails(Resource):
    """
    This will return data details.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, data_type):
        """
        Returns data details.
        """
        dt = dtyp.get_data_type_details(data_type)
        if dt is not None:
            return {data_type: dtyp.get_data_type_details(data_type)}
        else:
            raise wz.NotFound(f'{data_type} not found.')


"""
Project endpoints
"""


@projects.route(PROJECT_LIST)
class ProjectList(Resource):
    """
    This will get currrent projects in list.
    """
    def get(self):
        """
        Returns current projects in list.
        """
        return {PROJECT_LIST_NM: pj.get_projects()}


@projects.route(PROJECT_DICT)
class ProjectDict(Resource):
    """
    This will get all projects.
    """
    def get(self):
        """
        Returns all projects in dictionary.
        """
        return {'Data': pj.get_projects_dict(),
                'Type': 'Data',
                'Title': 'Current Projects'}


@projects.route(f'{PROJECT_DETAILS}/<project>')
class ProjectDetails(Resource):
    """
    This will get details on a project.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, project):
        """
        Returns the details of a specific project (in dictionary)
        """
        pjd = pj.get_project_details(project)
        if pjd is not None:
            return {'project detail': pj.get_project_details(project)}
        else:
            raise wz.NotFound(f'{project} not found.')


@projects.route(PROJECT_ADD)
class AddProject(Resource):
    """
    Add a new project.
    """
    @api.expect(project_fields)
    def post(self):
        """
        Add a new project.
        """
        print(f'{request.json=}')
        name = request.json[pj.NAME]
        del request.json[pj.NAME]
        pj.add_project(name, request.json)
        return {MESSAGE: f'{name} is added.'}


change_field = api.model("ChangeProject", {
    pj.NAME: fields.String,
    pj.FIELD: fields.String,
    pj.VALUE: fields.Raw(),
})


@projects.route(PROJECT_CHANGE_FIELD)
class ChangeProject(Resource):
    """
    Change a field in a existing project.
    """
    @api.expect(change_field)
    def post(self):
        """
        Change details of a project.
        """
        print(f'{request.json=}')
        name = request.json[pj.NAME]
        field = request.json[pj.FIELD]
        val = request.json[pj.VALUE]
        pj.change_project_single_field(name, field, val)
        return {MESSAGE: 'Project changed.'}


@projects.route(f'{PROJECT_DELETE}/<project>')
class DeleteProject(Resource):
    """
    Delete a Project
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, project):
        """
        Delete a existing project from db
        """
        pjd = pj.get_project_details(project)
        if pjd is not None:
            pj.del_project(project)
            return {MESSAGE: f'{project} is deleted.'}
        else:
            raise wz.NotFound(f'{project} not found.')


upload_parser = reqparse.RequestParser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)


@projects.route(f'{PROJECT_ADD_FILE}/<name>/<filename>')
class ADDFILE(Resource):
    """
    add a FILE
    """
    @api.expect(upload_parser)
    def post(self, name, filename):
        args = upload_parser.parse_args()
        file = args['file']
        if file is not None:
            pj.add_file(name, filename, file)
            return {MESSAGE: 'file added'}
        else:
            raise wz.NotFound('file is None')


@projects.route(f'{PROJECT_DELETE_FILE}')
class DELETEFILE(Resource):
    """
    Delete a FILE
    """
    def post(self):
        name = request.json[pj.NAME]
        if pj.check_if_exist(name) and pj.check_file_if_exist(name):
            pj.delete_file(name)
            return {MESSAGE: 'file deleted'}
        else:
            return {MESSAGE: f'{name} not exist in projects or {name} not \
                    have file'}


@projects.route(f'{PROJECT_GET_FILE}/<project>/<if_send>')
class GETFILE(Resource):
    """
    Get existing file if if_send is 0 only send name of file
    """
    def get(self, project, if_send):
        file, filename = pj.get_file(project)
        if file:
            if if_send == '0':
                return {'filename': filename}
            file_content = file.read()
            file_obj = BytesIO(file_content)
            file_mimetype, encoding = mimetypes.guess_type(filename)
            return send_file(file_obj,
                             as_attachment=True,
                             attachment_filename=filename,
                             mimetype=file_mimetype)
        else:
            return {MESSAGE: f'{project} not found'}


"""
User endpoints
"""


@users.route(USER_LIST)
class UserList(Resource):
    def get(self):
        """
        Return all registered users in a list.
        """
        return {USER_LIST_NM: usr.get_users()}


@users.route(USER_DICT)
class UserDict(Resource):
    """
    This will get all registered users info in dict.
    """
    def get(self):
        """
        Returns all registered users login info in dict.
        """
        return {'Data': usr.get_users_dict(),
                'Type': 'Data',
                'Title': 'Registered users'}


@users.route(f'{USER_DETAILS}/<user_email>')
class UserDetails(Resource):
    """
    This will get details on a registered user.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, user_email):
        """
        Returns the details of a specific users
        """
        usr_d = usr.get_user_details(user_email)
        if usr_d is not None:
            return {"user detail": usr.get_user_details(user_email)}
        else:
            raise wz.NotFound(f'{user_email} not found.')


@users.route(USER_ADD)
class AddUser(Resource):
    """
    Add a user.
    """
    @api.expect(user_fields)
    def post(self):
        """
        Add a user.
        """
        print(f'{request.json=}')
        email = request.json[usr.EMAIL]
        del request.json[usr.EMAIL]
        usr.add_user(email, request.json)
        return {MESSAGE: f'User {email} is added.'}


@users.route(USER_LOGIN)
class LoginUser(Resource):
    """
    Log user in and retrun an auth key
    """
    @api.expect(login_user_fields)
    def post(self):
        """
        Login in and retrun an auth key
        """
        print(f'{request.json=}')
        email = request.json[usr.EMAIL]
        del request.json[usr.EMAIL]

        """ Check if the user exist """
        user_exist = usr.user_exists(email)
        if user_exist:

            """ Verify if input password match with db password """
            pwd_db = usr.get_user_password(email)
            pwd_ipt = request.json[usr.PW]
            del request.json[usr.PW]

            check = pbkdf2_sha256.verify(pwd_ipt, pwd_db)

            if check:
                return {"Auth-Key": pwd_db}

        return ({MESSAGE: "Your login credentials are invalid"})


@users.route(USER_SIGNUP)
class SignupUser(Resource):
    """
    Create user and retrun an auth key
    """
    @api.expect(user_fields)
    def post(self):
        """
        Create user and retrun an auth key
        """
        print(f'{request.json=}')
        email = request.json[usr.EMAIL]
        del request.json[usr.EMAIL]

        """
        Check for same email address
        """
        if usr.user_exists(email):
            return ({MESSAGE: "Email already existed"})

        """ Encrypt password"""
        pwd = request.json[usr.PW]
        pwd_auth = pbkdf2_sha256.hash(pwd)
        request.json[usr.PW] = pwd_auth

        """ Add user """
        usr.add_user(email, request.json)

        return {"Auth-Key": pwd_auth}


@users.route(f'{USER_UPDATE}')
class UserUpdate(Resource):
    """
    This will replace the user details in db with updated info
    """
    @api.expect(user_fields)
    def post(self):
        """
        Replace the user details in db with updated info
        """
        print(f'{request.json=}')
        email = request.json[usr.EMAIL]
        del request.json[usr.EMAIL]
        """
        Check if the email address exists
        """
        user_exist = usr.user_exists(email)
        if user_exist:
            """
            Delete current account info, and replace with new
            """
            usr.del_user(email)

            pwd = request.json[usr.PW]
            pwd_auth = pbkdf2_sha256.hash(pwd)
            request.json[usr.PW] = pwd_auth

            usr.add_user(email, request.json)
            return {MESSAGE: f'User {email} : info updated.'}
        else:
            return ({MESSAGE: "Account not existed"})


@users.route(f'{USER_DELETE}/<user_email>')
class UserDelete(Resource):
    """
    This will delete a existing user.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, user_email):
        """
        Delete a existing user from db
        """
        usr_d = usr.get_user_details(user_email)
        if usr_d is not None:
            usr.del_user(user_email)
            return {MESSAGE: f'{user_email} is deleted.'}
        else:
            raise wz.NotFound({MESSAGE: f'{user_email} not found.'})

# @users.route('/',  methods=("POST", "GET"))
# class uploadImage():
#     """
#     This will allow user to upload images.
#     """

#     @api.expect(user_fields)
#     def post():
#         if request.method == 'POST':
#             # Upload file flask
#             uploaded_img = request.files['uploaded-file']
#             # Extracting uploaded data file name
#             img_filename = secure_filename(uploaded_img.filename)
#             # Upload file to database (defined uploaded folder in static path)
#             uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
#             # Storing uploaded file path in flask session
#             session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)
    
#             return render_template('index_upload_and_show_data_page2.html')
 
# @users.route('/show_image')
# class displayImage():
#     """
#     This will show the profile image.
#     """

#     @api.expect(user_fields)
#     def post():
#     # Retrieving uploaded file path from session
#         img_file_path = session.get('uploaded_img_file_path', None)
#         # Display image in Flask application web page
#         return render_template('show_image.html', user_image = img_file_path)

"""Application Endpoints"""


@applications.route(APPLICATION_DICT)
class ApplicationDict(Resource):
    """
    This will get all applications and reuturn in dictionary.
    """
    def get(self):
        """
        Returns all applications stored in db.
        """
        all_apl = apl.get_applications()

        if all_apl is not None:
            return {'Data': apl.get_applications_dict(),
                    'Type': 'Data',
                    'Title': 'all applications'}
        else:
            return ({MESSAGE: "No application existed."})


@applications.route(f'{APPLICATION_USER}/<user_email>')
class ApplicationUser(Resource):
    """
    This will get a particular user's applications.
    """
    def get(self, user_email):
        """
        Returns all applications of a particular user.
        """
        user_apl = apl.get_user_application(user_email)

        if user_apl is not None:
            return {f'{user_email}': user_apl}
        else:
            return ({MESSAGE: f'{user_email} has no valid applications.'})


@applications.route(f'{APPLICATION_PROJECT}/<project_name>')
class ApplicationProject(Resource):
    """
    This will get all applications of a particular project.
    """
    def get(self, project_name):
        """
        Returns all applications of a particular project.
        """
        proj_apl = apl.get_project_application(project_name)

        if proj_apl is not None:
            return {f'{project_name}': proj_apl}
        else:
            return ({MESSAGE: f'{project_name} has no valid applications.'})


@applications.route(f'{APPLICATION_DETAILS}/<application_name>')
class ApplicationDetails(Resource):
    """
    This will get details of a specific application.
    """
    def get(self, application_name):
        """
        Returns the details of a specific application.
        """
        apl_d = apl.get_application_details(application_name)

        if apl_d is not None:
            return {f'{application_name}': apl_d}
        else:
            return ({MESSAGE: f'{application_name} not found.'})


@applications.route(f'{APPLICATION_DELETE}/<application_name>')
class ApplicationDelete(Resource):
    """
    This will delete a existing application.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def post(self, application_name):
        """
        Delete a existing application from db
        """
        apld = apl.get_application_details(application_name)
        if apld is not None:
            apl.del_application(application_name)
            return {MESSAGE: f'{application_name} is deleted.'}
        else:
            raise wz.NotFound(f'{application_name} not found.')


@applications.route(APPLICATION_ADD)
class AddApplication(Resource):
    """
    Add an application.
    """
    @api.expect(application_fields)
    def post(self):
        """
        Add an application.
        """
        print(f'{request.json=}')
        apl_name = request.json[apl.NAME]
        apl_project = request.json[apl.PROJECT]

        """ Check if the application name is used """
        if apl.application_exists(apl_name):
            return ({MESSAGE: "The application name is already existed"})

        """ Check if the applied project exists """
        if pj.check_if_exist(apl_project):
            apl.add_application(apl_name, request.json)
            return {MESSAGE: f'Your application {apl_name} is added.'}
        else:
            return {MESSAGE: f'Project {apl_project} is not existed.'}


"""
List all endpoints
"""


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = ''
        # sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "sx2109@nyu.edu"
SMTP_PASSWORD = "Xsy12061045"
EMAIL_FROM = "sx2109@nyu.edu"
EMAIL_SUBJECT = "You have successfully registered. "
EMAIL_BODY = "You have successfully registered."

@api.route('/register')
class UserRegister(Resource):
    def post(self):

        # When register a new user
        # Send email notification
        user_email = request.json.get('email')
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = user_email
        msg['Subject'] = EMAIL_SUBJECT
        msg.attach(MIMEText(EMAIL_BODY))
        mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        mail.starttls()
        mail.login(SMTP_USERNAME, SMTP_PASSWORD)
        mail.sendmail(EMAIL_FROM, user_email, msg.as_string())
        mail.quit()

        return {MESSAGE: "User registered
        successfully."}, HTTPStatus.CREATED

'''
