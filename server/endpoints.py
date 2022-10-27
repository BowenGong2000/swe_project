"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask, request
from flask_restx import Resource, Api, fields
import db.data_type as dtyp
import db.projects as pj
import werkzeug.exceptions as wz

app = Flask(__name__)
api = Api(app)

LIST = 'list'
HELLO = '/hello'
MESSAGE = 'message'
DETAILS = 'details'
DATA_NS = 'data'
ADD = 'add'
DATA_LIST = f'/{DATA_NS}/{LIST}'
DATA_LIST_NM = '{DATA_NS}_list'
DATA_DETAILS = f'/{DATA_NS}/{DETAILS}'

PROJECTS_NS = 'projects'
PROJECT_LIST = f'/{PROJECTS_NS}/{LIST}'
PROJECT_LIST_NM = '{PROJECTS_NS}_list'
PROJECT_DETAILS = f'/{PROJECTS_NS}/{DETAILS}'
PROJECT_ADD = f'/{PROJECTS_NS}/{ADD}'

STUDENTS_NS = 'students'
STUDENT_LIST = f'/{STUDENTS_NS}/{LIST}'
STUDENT_LIST_NM = '{STUDENTS_NS}_list'
STUDENT_DETAILS = f'/{STUDENTS_NS}/{DETAILS}'
SPONSORS_NS = 'sponsors'
SPONSOR_LIST = f'/{SPONSORS_NS}/{LIST}'
SPONSOR_LIST_NM = '{SPONSORS_NS}_list'
SPONSOR_DETAILS = f'/{SPONSORS_NS}/{DETAILS}'


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


@api.route(DATA_LIST)
class DataList(Resource):
    """
    This will get a list of data names
    """
    def get(self):
        """
        Return a list of data names
        """
        return {DATA_LIST_NM: dtyp.get_data_types()}


@api.route(f'{DATA_DETAILS}/<data_type>')
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


@api.route(PROJECT_LIST)
class ProjectList(Resource):
    """
    This will get a list of currrent projects.
    """
    def get(self):
        """
        Returns a list of current projects.
        """
        return {PROJECT_LIST_NM: pj.get_projects()}


@api.route(f'{PROJECT_DETAILS}/<project>')
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


@api.route(PROJECT_ADD)
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
        Return the message if a project is added successuflly. (new project page)
        """
        return {MESSAGE: 'Successfully added a new project.'}


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
