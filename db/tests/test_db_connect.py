
import pymongo as pm
import pytest
import db.db_connect as dbc
import os

TEST_DB = dbc.PROJECT_DB
TEST_COLLECT = 'test_collect'

TEST_NAME = 'test'
RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)

@pytest.fixture(scope='function')
def temp_rec():
    if not RUNNING_ON_CICD_SERVER:
        dbc.connect_db()
        dbc.client[TEST_DB][TEST_COLLECT].insert_one({TEST_NAME: TEST_NAME})
        # yield to our test function
        yield
        dbc.client[TEST_DB][TEST_COLLECT].delete_one({TEST_NAME: TEST_NAME})
    else:
        yield
        return True
