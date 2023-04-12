import os
import pytest
import db.projects as pj

TEST_DEL_NAME = 'Test Project Del'
TEST_USER_ACCOUNT = 'yzzzz@nyu.edu'
RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)


def create_project_details():
    details = {}
    for field in pj.REQUIRED_FLDS:
        details[field] = 2
    return details


@pytest.fixture(scope='function')
def to_be_del_project():
    return pj.add_project(TEST_DEL_NAME, create_project_details())


def test_del_project(to_be_del_project):
    pj.del_project(TEST_DEL_NAME)
    assert not pj.check_if_exist(TEST_DEL_NAME)


@pytest.fixture(scope='function')
def temp_project():
    pj.add_project(pj.TEST_PROJECT_NAME, create_project_details())
    yield    # to test functions 
    pj.del_project(pj.TEST_PROJECT_NAME)


def test_get_projects(temp_project):
    if not RUNNING_ON_CICD_SERVER:
        pjs = pj.get_projects()
        assert isinstance(pjs, list)
        assert len(pjs) > 0


def test_get_project_details(temp_project):
    if not RUNNING_ON_CICD_SERVER:
        pj_dtls = pj.get_project_details(pj.TEST_PROJECT_NAME)
        assert isinstance(pj_dtls, dict)


def test_get_projects_dict(temp_project):
    if not RUNNING_ON_CICD_SERVER:
        pjs = pj.get_projects_dict()
        assert isinstance(pjs, dict)
        assert len(pjs) > 0


def test_project_exists(temp_project):
    assert pj.check_if_exist(pj.TEST_PROJECT_NAME)


def test_project_not_exists():
    assert not pj.check_if_exist('Surely this is not a project name!')


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        pj.add_project(7, {})


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        pj.add_project('a new project', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        pj.add_project('a new project', {'foo': 'bar'})


def test_add_project():
    if not RUNNING_ON_CICD_SERVER:
        pj.add_project(pj.TEST_PROJECT_NAME, create_project_details())
        assert pj.check_if_exist(pj.TEST_PROJECT_NAME)
        pj.del_project(pj.TEST_PROJECT_NAME)


def test_get_project_num():
    if not RUNNING_ON_CICD_SERVER:
        num = pj.get_proj_num()
        assert isinstance(num, int)


def test_get_user_project():
    pjs = pj.get_user_project(TEST_USER_ACCOUNT)
    assert isinstance(pjs, list)
    for project in pjs:
        assert project['account']['email'] == TEST_USER_ACCOUNT


def test_change_project_single_field():
    pj.add_project(pj.TEST_PROJECT_NAME, create_project_details())
    the_pj = pj.change_project_single_field(pj.TEST_PROJECT_NAME, pj.APPROVE, False)
    assert the_pj[pj.APPROVE] == False
    pj.del_project(pj.TEST_PROJECT_NAME)