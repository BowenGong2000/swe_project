
import db.projects as pj


def test_get_projects():
    pjs = pj.get_projects()
    assert isinstance(pjs, list)
    assert len(pjs) > 1


def test_get_project_details():
    pj_dets = pj.get_project_details(pj.TEST_PROJECT_NAME)
    assert isinstance(pj_dets, dict)