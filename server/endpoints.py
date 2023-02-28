"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask, request
from flask_restx import Resource, Api, fields, Namespace, reqparse
from passlib.hash import pbkdf2_sha256
from werkzeug.datastructures import FileStorage

import db.data_type as dtyp
import db.projects as pj
import db.sponsors as sps
import db.user as usr

import werkzeug.exceptions as wz


app = Flask(__name__)
api = Api(app)

DATA_NS = 'data'
PROJECTS_NS = 'projects'
USERS_NS = 'users'
SPONSORS_NS = 'sponsors'

data_types = Namespace(DATA_NS, 'Data Types')
api.add_namespace(data_types)
projects = Namespace(PROJECTS_NS, 'Projects')
api.add_namespace(projects)
users = Namespace(USERS_NS, 'Users')
api.add_namespace(users)
sponsors = Namespace(SPONSORS_NS, 'Sponsors')
api.add_namespace(sponsors)

LIST = 'list'
DICT = 'dict'
HELLO = '/hello'
MESSAGE = 'message'
DETAILS = 'details'
ADD = 'add'
CHANGE = 'change'
DELETE = 'delete'
FILE = "file"

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
PROJECT_CHANGE_FILE = f"/{FILE}/{CHANGE}"

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

SPONSOR_DICT = f'/{DICT}'
SPONSOR_DICT_NM = f'{SPONSORS_NS}_dict'
SPONSOR_DICT_W_NS = f'{SPONSORS_NS}/{DICT}'
SPONSOR_DETAILS = f'/{DETAILS}'
SPONSOR_DETAILS_W_NS = f'{SPONSORS_NS}/{DETAILS}'
SPONSOR_LIST = f'/{LIST}'
SPONSOR_LIST_NM = f'{SPONSORS_NS}_list'
SPONSOR_LIST_W_NS = f'{SPONSORS_NS}/{LIST}'
SPONSOR_ADD = f'/{SPONSORS_NS}/{ADD}'


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
                    '3': {'url': f'/{SPONSOR_DICT_W_NS}',
                          'method': 'get',
                          'text': 'List Sponsors.'},
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
    This will get currrent projects.
    """
    def get(self):
        """
        Returns current projects in dictionary.
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


change_field = api.model("ChangeProject",{
    pj.NAME: fields.String,
    pj.FIELD: fields.String,
    pj.VALUE: fields.Raw(),
})


@projects.route(PROJECT_CHANGE_FIELD)
class ChangeProject(Resource):
    """
    change a feild in a exist project.
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
        #file = request.files[pj.FILE]
        args = upload_parser.parse_args()
        file = args['file']
        if file is not None:
            pj.add_file(name, filename, file)
            return {MESSAGE: f'file added'}
        else:
            raise wz.NotFound(f'file is None')


@projects.route(f'{PROJECT_DELETE_FILE}')
class DELETEFILE(Resource):
    """
    delete a FILE
    """
    def post(self):
        name = request.json[pj.NAME]
        if pj.check_if_exist(name) and pj.check_file_if_exist(name):
            pj.delete_file(name)
            return {MESSAGE: f'file deleted'}
        else:
            return {MESSAGE: f'{name} not exist in projects or {name} not have file'}
        

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
        Check if the email address exist
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
            raise wz.NotFound(f'{user_email} not found.')


"""Sponsor Endpoints"""


@sponsors.route(SPONSOR_LIST)
class SponsorList(Resource):
    def get(self):
        return {SPONSOR_LIST_NM: sps.get_sponsors()}


@sponsors.route(SPONSOR_DICT)
class SponsorDict(Resource):
    """
    This will get a list of participating sponsors.
    """
    def get(self):
        """
        Returns a list of participating sponsors.
        """
        return {'Data': sps.get_sponsors_dict(),
                'Type': 'Data',
                'Title': 'Paricipating Sponsors'}


@sponsors.route(f'{SPONSOR_DETAILS}/<sponsor>')
class SponsorDetails(Resource):
    """
    This will get details on a sponsor.
    """
    @api.response(HTTPStatus.OK, 'Success')
    @api.response(HTTPStatus.NOT_FOUND, 'Not Found')
    def get(self, sponsor):
        """
        Returns the details of a specific sponsor (in dictionary)
        """
        sps_d = sps.get_sponsor_details(sponsor)
        if sps_d is not None:
            return {sponsor: sps.get_sponsor_details(sponsor)}
        else:
            raise wz.NotFound(f'{sponsor} not found.')


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
