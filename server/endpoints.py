"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask, request
from flask_restx import Resource, Api, fields, Namespace

import db.data_type as dtyp
import db.projects as pj
import db.students as std
import werkzeug.exceptions as wz

app = Flask(__name__)
api = Api(app)

DATA_NS = 'data'
PROJECTS_NS = 'projects'
STUDENTS_NS = 'students'
SPONSORS_NS = 'sponsors'

data_types = Namespace(DATA_NS, 'Data Types')
api.add_namespace(data_types)
projects = Namespace(PROJECTS_NS, 'Projects')
api.add_namespace(projects)
students = Namespace(STUDENTS_NS, 'Students')
api.add_namespace(students)

LIST = 'list'
DICT = 'dict'
HELLO = '/hello'
MESSAGE = 'message'
DETAILS = 'details'
ADD = 'add'

MAIN_MENU = '/main_menu'
MAIN_MENU_NM = 'Main Menu'

DATA_LIST = f'/{LIST}'
DATA_LIST_NM = f'{DATA_NS}_list'
DATA_LIST_W_NS = f'{DATA_NS}/{LIST}'
DATA_DETAILS = f'/{DETAILS}'
DATA_DETAILS_W_NS = f'{DATA_NS}/{DETAILS}'

PROJECT_DICT = f'/{DICT}'
PROJECT_DICT_NM = f'{PROJECTS_NS}_dict'
PROJECT_DICT_W_NS = f'{PROJECTS_NS}/{DICT}'

PROJECT_LIST = f'/{LIST}'
PROJECT_LIST_NM = f'{PROJECTS_NS}_list'
PROJECT_LIST_W_NS = f'{PROJECTS_NS}/{LIST}'
PROJECT_DETAILS = f'/{DETAILS}'
PROJECT_DETAILS_W_NS = f'{PROJECTS_NS}/{DETAILS}'
PROJECT_ADD = f'/{PROJECTS_NS}/{ADD}'

STUDENT_LIST = f'/{LIST}'
STUDENT_LIST_NM = f'{STUDENTS_NS}_list'
STUDENT_LIST_W_NS = f'/{STUDENTS_NS}/{LIST}'

SPONSOR_LIST = f'/{SPONSORS_NS}/{LIST}'
SPONSOR_LIST_NM = f'{SPONSORS_NS}_list'


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
                'Default': 0,
                'Choices': {
                    '1': {'url' : '/projects/dict',
                          'method' : 'get',
                          'text' : 'List Current Projects.'},
                    '2': {'text': 'List Students.'},
                    '3': {'text': 'List Sponsors.'},
                    'X': {'text': 'Exit'},
                }}


@data_types.route(DATA_LIST)
class DataList(Resource):
    """
    This will get a list of data names
    """
    def get(self):
        """
        Return a list of data names
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
                'Type' : 'Data',
                'Title': 'Current Projects'}

@projects.route(PROJECT_LIST)
class ProjectDict(Resource):
    """
    This will get currrent projects in list.
    """
    def get(self):
        """
        Returns current projects in list.
        """
        return {PROJECT_LIST_NM: pj.get_projects()}


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
            return {project: pj.get_project_details(project)}
        else:
            raise wz.NotFound(f'{project} not found.')


project_fields = api.model('NewProject1', {
    pj.NAME: fields.String,
    pj.NUM_MEMBERS: fields.Integer,
    pj.DEPARTMENT: fields.String,
    pj.MAJOR: fields.String,
    pj.SCHOOL_YEAR: fields.String,
    pj.GPA: fields.Float,
    pj.LENGTH: fields.String,
    pj.SKILL: fields.String
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
        return {MESSAGE: 'Project added.'}

    def get(self):
        """
        Return the message if a project is added successuflly.
        """
        return {MESSAGE: 'Successfully added a new project.'}


@students.route(STUDENT_LIST)
class StudentList(Resource):
    """
    This will get a list of participating students.
    """
    def get(self):
        """
        Returns a list of participating students.
        """
        return {STUDENT_LIST_NM: std.get_students()}


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
