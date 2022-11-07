import pytest

from app import app
import db.projects as pj

TEST_CLIENT = app.test_client()
TEST_PROJECT_NAME = 'Test project'
TEST_PROJECT  = pj.projects[TEST_PROJECT_NAME]

def test_homepage():
    """
    when the '/' page is requested,
    see if the response is valid
    """
    response = TEST_CLIENT.get('/')
    assert response.status_code == 200
    assert response.get_data(as_text=True)
    response_post = TEST_CLIENT.post('/')
    assert response_post.status_code == 405

def test_add_project():
    """
    when the '/add_project' page is requested (GET),
    see if the response is valid
    """ 
    response_get = TEST_CLIENT.get('/add_project')
    assert response_get.status_code == 200
    assert pj.check_if_exist(TEST_PROJECT_NAME)
    pj.del_project(TEST_PROJECT_NAME)
