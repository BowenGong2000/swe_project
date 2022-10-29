
import pytest

import server.endpoints as ep
import db.projects as pj
import db.students as st

TEST_CLIENT = ep.app.test_client()
TEST_DATA_TYPE = 'Student'
TEST_PROJECT_NAME = 'Test project'
TEST_PROJECT  = pj.projects[TEST_PROJECT_NAME]

def test_hello():
    """
    see if Hello works
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)

def test_add_project():
    """
    see if adding project works properly.
    """
    resp = TEST_CLIENT.post(ep.PROJECT_ADD, json=TEST_PROJECT)
    assert pj.check_if_exist(TEST_PROJECT_NAME)
    pj.del_project(TEST_PROJECT_NAME)

def test_get_ProjectList(): 
    """
    see if we can get project list properly
    should be store in a list and return a list
    """
    resp_json = TEST_CLIENT.get(ep.PROJECT_LIST_W_NS).get_json()
    assert isinstance(resp_json[ep.PROJECT_LIST_NM], list) 

def test_get_ProjectList_not_empty():
    """
    see if the project list has something in it
    """
    resp_json = TEST_CLIENT.get(ep.PROJECT_LIST_W_NS).get_json()
    assert len(resp_json[ep.PROJECT_LIST_NM]) > 0

def test_get_project_type_details():
    """
    see if we can get project details properly
    """
    resp_json = TEST_CLIENT.get(f'{ep.PROJECT_DETAILS_W_NS}/{TEST_PROJECT}').get_json()
    assert isinstance(resp_json, dict)

SAMPLE_STUDENT_NM = 'SampleStudent'
SAMPLE_STUDENT = {
    st.FULL_NAME: 'Sample User',
    st.PHONE: 11111111,
    st.EMAIL: 'xx@nyu.com',
    st.MAJOR: 'CE',
    st.SCHOOL_YEAR: 'Junior',
    st.GPA: 3.9,
    st.SKILL: 'design'
}

def test_get_student_list():
    """
    See if we can get a student list properly.
    Return should look like:
        {STUDENT_LIST_NM: [list of students...]}
    """
    resp = TEST_CLIENT.get(ep.STUDENT_LIST)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.STUDENT_LIST_NM], list)

def test_get_student_type_details():
    """
    see if we can get student details properly
    """
    resp_json = TEST_CLIENT.get(f'{ep.STUDENT_DETAILS_W_NS}/{TEST_STUDENT}').get_json()
    assert isinstance(resp_json, dict)

def test_get_DataList(): 
    """
    see if we can get data list properly
    Return should look like:
        {DATA_LIST_NM: [list of data ...]}
    """
    resp_json = TEST_CLIENT.get(ep.DATA_LIST_W_NS).get_json()
    assert isinstance(resp_json[ep.DATA_LIST_NM], list)

def test_get_DataList_not_empty():
    """
    see if we can get data list properly
    Return should look like:
        {DATA_LIST_NM: [list of data ...]}
    """
    resp_json = TEST_CLIENT.get(ep.DATA_LIST_W_NS).get_json()
    assert len(resp_json[ep.DATA_LIST_NM]) > 0

def test_get_data_type_details():
    """
    see if we can get data type details properly
    """
    resp_json = TEST_CLIENT.get(f'{ep.DATA_DETAILS_W_NS}/{TEST_DATA_TYPE}').get_json()
    assert TEST_DATA_TYPE in resp_json
    assert isinstance(resp_json[TEST_DATA_TYPE], dict) #store as disctionary