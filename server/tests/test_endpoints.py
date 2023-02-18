
import pytest

import server.endpoints as ep
import db.projects as pj
import db.user as usr
import db.sponsors as sps

TEST_CLIENT = ep.app.test_client()
TEST_DATA_TYPE = 'Project'

TEST_PROJECT_NAME = 'Test project'
TEST_PROJECT  = pj.projects[TEST_PROJECT_NAME]

TEST_USER_EMAIL = 'Test'
TEST_USER = usr.users[TEST_USER_EMAIL]

TEST_SPONSOR_NAME = 'Test sponsor'
TEST_SPONSOR = sps.sponsors[TEST_SPONSOR_NAME]

# Need to add more tests for projects and users

def test_hello():
    """
    see if Hello works
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


# Tests for Projects

# def test_add_project():
#     """
#     see if adding project works properly.
#     """
#     resp = TEST_CLIENT.post(ep.PROJECT_ADD, json=TEST_PROJECT)
#     assert pj.check_if_exist(TEST_PROJECT_NAME)
#     pj.del_project(TEST_PROJECT_NAME)

def test_get_project_details():
    resp_json = TEST_CLIENT.get(f'{ep.PROJECT_DETAILS_W_NS}/{TEST_PROJECT}').get_json()
    assert isinstance(resp_json, dict)



# Tests for user login in
def test_get_users_dict():
    """
    see if we can get users properly in a dictionary
    """
    users = usr.get_users_dict()
    assert isinstance(users, dict)
    assert len(users) > 0

def test_get_user_details():
    """
    see if we can get a user login info properly
    """
    resp_json = TEST_CLIENT.get(f'{ep.USER_DETAILS_W_NS}/{TEST_USER}').get_json()
    assert isinstance(resp_json, dict)

# Tests for Sponsors
def test_get_sponsors_list():
    resp_json = TEST_CLIENT.get(ep.SPONSOR_LIST_W_NS).get_json()
    assert isinstance(resp_json[ep.SPONSOR_LIST_NM], list)

def test_get_sponsors_dict():
    """
    see if we can get sponsors properly in a dictionary
    """
    sponsors = sps.get_sponsors_dict()
    assert isinstance(sponsors, dict)
    assert len(sponsors) > 0

def test_get_sponsor_details():
    """
    see if we can get sponsor details properly
    """
    resp_json = TEST_CLIENT.get(f'{ep.SPONSOR_DETAILS_W_NS}/{TEST_SPONSOR}').get_json()
    assert isinstance(resp_json, dict)

# Tests for Datatypes
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