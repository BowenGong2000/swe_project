
import pytest
from http import HTTPStatus
from passlib.hash import pbkdf2_sha256
import uuid

import server.endpoints as ep
import db.projects as pj
import db.user as usr
import db.application as apl


TEST_CLIENT = ep.app.test_client()
TEST_DATA_TYPE = 'Project'

TEST_PROJECT_NAME = 'Test project'
TEST_PROJECT = {
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

TEST_CHANGE_PROJECT = {
    pj.NAME: "sample project",
    pj.FIELD: "if_approve",
    pj.VALUE: False
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
TEST_NEW_USER = {
    usr.NAME: 'new',
    usr.EMAIL: TEST_USER_EMAIL,
    usr.PHONE: 'new',
    usr.PW: 'new',
}
TEST_BAD_USER_EMAIL = "bad"

TEST_APPLICATION_NAME = 'test app name'
TEST_APPLICATION = {
    apl.NAME: TEST_APPLICATION_NAME,
    apl.APPLICANT_NAME: 'test name',
    apl.APPLICANT_EMAIL: TEST_USER_EMAIL,
    apl.PROJECT: TEST_PROJECT_NAME,
    apl.APP_DATE: '2022-06-08',
    apl.RESUME: '123',
    apl.TRANSCRIPT: '123',
    apl.APP_STATUS: 'Processing',
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

def test_change_project():
    """
    check if change field work
    """
    resp = TEST_CLIENT.post(f'{ep.PROJECTS_NS}{ep.PROJECT_CHANGE_FIELD}', json=TEST_CHANGE_PROJECT)

def test_get_project_details():
    """
    See if we can get the details of a project properly
    """
    resp_json = TEST_CLIENT.get(f'{ep.PROJECT_DETAILS_W_NS}/{TEST_PROJECT}').get_json()
    assert isinstance(resp_json, dict)
    assert len(resp_json) > 0

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

def test_delete_project():
    """
    Check if project can be deleted properly
    """
    pj.add_project(TEST_PROJECT_NAME, TEST_PROJECT)
    resp = TEST_CLIENT.post(f'/{ep.PROJECTS_NS}{ep.PROJECT_DELETE}/{TEST_PROJECT_NAME}')
    assert pj.check_if_exist(TEST_PROJECT_NAME) == False


"""
Tests for Users
"""

def test_get_user_dict():
    """
    See if we can get all users info properly.
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
    assert len(resp_json) > 0

def test_get_missing_user_details():
    """
    See if we can get error message if a missing user is entered
    """
    resp = TEST_CLIENT.get(f'{ep.USER_DETAILS_W_NS}/{TEST_BAD_USER_EMAIL}')
    assert resp.status_code == HTTPStatus.NOT_FOUND

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

def test_signup_user():
    """
    Make sure the user is not existed in db before.
    """
    usr.del_user(TEST_USER_EMAIL)
    assert usr.user_exists(TEST_USER_EMAIL) == False
    """
    See if signup works properly.
    """
    resp = TEST_CLIENT.post(f'/{ep.USERS_NS}{ep.USER_SIGNUP}', json=TEST_USER)
    assert usr.user_exists(TEST_USER_EMAIL) == True
    assert len(usr.get_user_details(TEST_USER_EMAIL)) > 0
    usr.del_user(TEST_USER_EMAIL)

def test_delete_user():
    """
    Check if user can be deleted properly
    """
    usr.add_user(TEST_USER_EMAIL, TEST_USER)
    resp = TEST_CLIENT.post(f'/{ep.USERS_NS}{ep.USER_DELETE}/{TEST_USER_EMAIL}')
    assert usr.user_exists(TEST_USER_EMAIL) == False
    
def test_update_user():
    """
    Check if user info can be updated properly
    """
    usr.add_user(TEST_USER_EMAIL, TEST_USER)
    resp = TEST_CLIENT.post(f'/{ep.USERS_NS}{ep.USER_UPDATE}', json=TEST_NEW_USER)
    
    db_name = usr.get_user_details(TEST_USER_EMAIL)["name"]
    db_phone = usr.get_user_details(TEST_USER_EMAIL)["phone"]

    assert db_name == TEST_NEW_USER['name']
    assert db_phone == TEST_NEW_USER['phone']

    usr.del_user(TEST_USER_EMAIL)


"""
Tests for Applications
"""
def test_get_applications_list():
    """
    See if we can get all applications and return in a list.
    """
    resp = TEST_CLIENT.get(ep.APPLICATION_LIST_W_NS)
    resp_json = resp.get_json()[ep.APPLICATION_LIST_NM]
    assert isinstance(resp_json, list)
    assert len(resp_json) > 0


def test_get_applications_dict():
    """
    See if we can get all applications info properly.
    Return should look like:
        {Data: {all existing applications...}}
    """
    resp = TEST_CLIENT.get(ep.APPLICATION_DICT_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json['Data'], dict)
    """
    Test if the dict is not empty.
    """
    assert len(resp_json['Data']) > 0


def test_get_application_details():
    """
    See if we can get application details by name
    """
    resp_json = TEST_CLIENT.get(f'{ep.APPLICATION_DETAILS_W_NS}/{TEST_APPLICATION_NAME}').get_json()
    assert isinstance(resp_json, dict)
    assert len(resp_json) > 0


def test_get_user_application():
    """
    See if we can get applications by user
    """
    resp_json = TEST_CLIENT.get(f'{ep.APPLICATION_USER_W_NS}/{TEST_USER_EMAIL}').get_json()
    assert isinstance(resp_json, dict)
    assert len(resp_json) > 0


def test_delete_application():
    """
    Check if application can be deleted properly
    """
    apl.add_application(TEST_APPLICATION_NAME, TEST_APPLICATION)
    resp = TEST_CLIENT.post(f'/{ep.APPLICATION_NS}{ep.APPLICATION_DELETE}/{TEST_APPLICATION_NAME}')
    assert apl.application_exists(TEST_APPLICATION_NAME) == False


"""
Tests for Data Types
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
    assert isinstance(resp_json[TEST_DATA_TYPE], dict) 