import pytest
import os
import db.projects as pj


RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)


def test_get_projects():
    pjs = pj.get_projects()
    assert isinstance(pjs, list)
    assert len(pjs) > 1


def test_get_project_details():
    pj_dets = pj.get_project_details(pj.TEST_PROJECT_NAME)
    assert isinstance(pj_dets, dict)


def test_get_projects_dict():
    if not RUNNING_ON_CICD_SERVER:
        pjs = pj.get_projects_dict()
        assert isinstance(pjs, dict)
        assert len(pjs) > 1


def test_add_project():
    details = {}
    for field in pj.REQUIRED_FLDS:
        details[field] = 'TEST'
    pj.add_project(pj.TEST_PROJECT_NAME, details)
    assert pj.check_if_exist(pj.TEST_PROJECT_NAME)
    pj.del_project(pj.TEST_PROJECT_NAME)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        pj.add_project(7, {})


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        pj.add_project('a new project', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        pj.add_project('a new project', {'foo': 'bar'})