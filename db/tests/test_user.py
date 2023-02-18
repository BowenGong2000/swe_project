import pytest
import os
import db.user as us

TEST_DEL_NAME = 'Test User Del'
RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)


def create_user_details():
    details = {}
    for field in us.REQUIRED_FLDS:
        details[field] = 2
    return details


@pytest.fixture(scope='function')
def to_be_del_user():
    return us.add_user(TEST_DEL_NAME, create_user_details())


def test_del_user(to_be_del_user):
    us.del_user(TEST_DEL_NAME)
    assert not us.user_exists(TEST_DEL_NAME)


@pytest.fixture(scope='function')
def temp_user():
    us.add_user(us.TEST_USER_EMAIL, create_user_details())
    yield    # to test functions 
    us.del_user(us.TEST_USER_EMAIL)


def test_get_users(temp_user):
    if not RUNNING_ON_CICD_SERVER:
        uss = us.get_users()
        assert isinstance(uss, list)
        assert len(uss) > 0


def test_get_user_details(temp_user):
    if not RUNNING_ON_CICD_SERVER:
        us_dtls = us.get_user_details(us.TEST_USER_EMAIL)
        assert isinstance(us_dtls, dict)


def test_get_users_dict(temp_user):
    if not RUNNING_ON_CICD_SERVER:
        uss = us.get_users_dict()
        assert isinstance(uss, dict)
        assert len(uss) > 0


def test_user_exists(temp_user):
    assert us.user_exists(us.TEST_USER_EMAIL)


def test_user_not_exists():
    assert not us.user_exists('User does not exist!')


def test_add_user():
    if not RUNNING_ON_CICD_SERVER:
        us.add_user(us.TEST_USER_EMAIL, create_user_details())
        assert us.user_exists(us.TEST_USER_EMAIL)
        us.del_user(us.TEST_USER_EMAIL)