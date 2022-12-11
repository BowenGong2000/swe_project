import pytest
# import os
import db.projects as pj


# RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)


def create_project_details():
    details = {}
    for field in pj.REQUIRED_FLDS:
        details[field] = 2
    return details


@pytest.fixture(scope='function')
def temp_project():
    pj.add_project(pj.TEST_PROJECT_NAME, create_project_details())
    yield
    return True


def test_get_projects(temp_project):
    pjs = pj.get_projects()
    assert isinstance(pjs, list)
    assert len(pjs) > 0


def test_get_project_details(temp_project):
    pj_dtls = pj.get_project_details(pj.TEST_PROJECT_NAME)
    assert isinstance(pj_dtls, dict)


def test_get_projects_dict(temp_project):
    pjs = pj.get_projects_dict()
    assert isinstance(pjs, dict)
    assert len(pjs) > 0


def test_add_project():
    pj.add_project(pj.TEST_PROJECT_NAME, create_project_details())


def test_project_exists(temp_project):
    assert pj.project_exists(pj.TEST_PROJECT_NAME)


def test_project_not_exists():
    assert not pj.project_exists('Surely this is not a project name!')


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
    pj.add_project(name, details)(pj.TEST_PROJECT_NAME, create_project_details())
