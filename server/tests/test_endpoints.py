
import pytest

import server.endpoints as ep
import db.projects as pj
import db.user as usr
import db.sponsors as sps
import uuid

TEST_CLIENT = ep.app.test_client()
TEST_DATA_TYPE = 'Project'

TEST_PROJECT_NAME = 'Test project'
TEST_PROJECT  = {
    pj.ACCOUNT: "test account",
    pj.NAME: 'Test project',
    pj.NUM_MEMBERS: 7,
    pj.DEPARTMENT: 'computer_engineering',
    pj.MAJOR: 'computer_science',
    pj.SCHOOL_YEAR: 'sophomore and beyond',
    pj.GPA: 0,
    pj.LENGTH: '4 months',
    pj.SKILL: 'C++, python',
    pj.DESCRIP: 'its a default message',
    pj.POST_DATE: '2022-06-08',
    pj.APPROVE: False
}

TEST_USER_EMAIL = 'test@nyu.edu'
TEST_USER = {
    "_id": uuid.uuid4().hex,
    usr.NAME: 'test name',
    usr.EMAIL: TEST_USER_EMAIL,
    usr.PHONE: '1234',
    usr.PW: '1234',
}
TEST_LOGIN_USER = {
    "_id": uuid.uuid4().hex,
    usr.EMAIL: TEST_USER_EMAIL,
    usr.PW: '1234',
}


def test_hello():
    """
    see if Hello works
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    print(pj.TEST_PROJECT_NAME)
    assert isinstance(resp_json[ep.MESSAGE], str)


"""
Tests for Projects
"""
def test_add_project():
    """
    See if adding project works properly.
    """
    resp = TEST_CLIENT.post(f'/{ep.PROJECTS_NS}{ep.PROJECT_ADD}', json=TEST_PROJECT)
    assert pj.check_if_exist(TEST_PROJECT_NAME)
    pj.del_project(TEST_PROJECT_NAME)

def test_get_project_details():
    """
    See if we can get the details of a project properly
    """
    resp_json = TEST_CLIENT.get(f'{ep.PROJECT_DETAILS_W_NS}/{TEST_PROJECT}').get_json()
    assert isinstance(resp_json, dict)

def test_get_project_dict():
    """
    See if we can get all projects info properly.
    Return should look like:
        {Data: {all projects...}}
    """
    resp = TEST_CLIENT.get(ep.PROJECT_DICT_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json['Data'], dict)
    """
    Test if the dict is not empty.
    """
    assert len(resp_json['Data']) > 0


"""
Tests for Users
"""

def test_get_user_dict():
    """
    See if we can get all projects info properly.
    Return should look like:
        {Data: {all existing user accounts...}}
    """
    resp = TEST_CLIENT.get(ep.USER_DICT_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json['Data'], dict)
    """
    Test if the dict is not empty.
    """
    assert len(resp_json['Data']) > 0

def test_get_user_details():
    """
    See if we can get a user's details properly
    """
    resp_json = TEST_CLIENT.get(f'{ep.USER_DETAILS_W_NS}/{TEST_USER}').get_json()
    assert isinstance(resp_json, dict)

def test_add_user():
    """
    See if adding user works properly.
    """
    resp = TEST_CLIENT.post(f'/{ep.USERS_NS}{ep.USER_ADD}', json=TEST_USER)
    assert usr.user_exists(TEST_USER_EMAIL)
    usr.del_user(TEST_USER_EMAIL)

def test_login_user():
    """
    See if login works properly.
    """
    usr.add_user(TEST_USER_EMAIL, TEST_LOGIN_USER)
    resp = TEST_CLIENT.post(f'/{ep.USERS_NS}{ep.USER_LOGIN}', json=TEST_LOGIN_USER)
    assert usr.user_exists(TEST_USER_EMAIL)

    pwd_db = usr.get_user_password(TEST_USER_EMAIL)
    assert pwd_db == TEST_USER["password"]
    usr.del_user(TEST_USER_EMAIL)



"""
Tests for Datatypes
"""
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