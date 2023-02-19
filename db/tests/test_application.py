import pytest
import os
import db.application as appl

TEST_DEL_NAME = 'Test Application Del'
RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)


def create_application_details():
    details = {}
    for field in appl.REQUIRED_FLDS:
        details[field] = 2
    return details


@pytest.fixture(scope='function')
def to_be_del_application():
    return appl.add_application(TEST_DEL_NAME, create_application_details())


def test_del_application(to_be_del_application):
    appl.del_application(TEST_DEL_NAME)
    assert not appl.application_exists(TEST_DEL_NAME)


@pytest.fixture(scope='function')
def temp_application():
    appl.add_application(appl.TEST_APPLICATION_NAME, create_application_details())
    yield    # to test functions 
    appl.del_application(appl.TEST_APPLICATION_NAME)


def test_get_applications(temp_application):
    if not RUNNING_ON_CICD_SERVER:
        appls = appl.get_applications()
        assert isinstance(appls, list)
        assert len(appls) > 0


def test_get_application_details(temp_application):
    if not RUNNING_ON_CICD_SERVER:
        appl_dtls = appl.get_application_details(appl.TEST_APPLICATION_NAME)
        assert isinstance(appl_dtls, dict)


def test_get_applications_dict(temp_application):
    if not RUNNING_ON_CICD_SERVER:
        appls = appl.get_applications_dict()
        assert isinstance(appls, dict)
        assert len(appls) > 0


def test_application_exists(temp_application):
    assert appl.application_exists(appl.TEST_APPLICATION_NAME)


def test_application_not_exists():
    assert not appl.application_exists('application does not exist!')


def test_add_application():
    if not RUNNING_ON_CICD_SERVER:
        appl.add_application(appl.TEST_APPLICATION_NAME, create_application_details())
        assert appl.application_exists(appl.TEST_APPLICATION_NAME)
        appl.del_application(appl.TEST_APPLICATION_NAME)