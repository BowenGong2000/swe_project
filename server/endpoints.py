"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from flask_restx import Resource, Api
import db.data_type as dtyp

app = Flask(__name__)
api = Api(app)

LIST = 'list'
HELLO = '/hello'
MESSAGE = 'message'
DETAILS = 'details'
DATA_LIST = f'/data_list/{LIST}'
DATA_LIST_NM = 'data_list'
DATA_TYPE_DETAILS = f'/data_list/{DETAILS}'



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


@api.route(f'{DATA_TYPE_DETAILS}/<data_type>')
class DataTypeDetails(Resource):
    """
    This will get a list of data types.
    """
    def get(self, data_type):
        """
        Returns a list of data types.
        """
        return {data_type: {}}


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
