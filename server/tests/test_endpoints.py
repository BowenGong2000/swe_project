
import pytest

import server.endpoints as ep
import db.projects as pj
import db.students as std
import db.sponsors as sps

TEST_CLIENT = ep.app.test_client()
TEST_DATA_TYPE = 'Student'


def test_hello():
    """
    see if Hello works
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)


SAMPLE_STUDENT_NM = 'SampleStudent'
SAMPLE_STUDENT = {
    std.EMAIL: 'email',
    std.PHONE: 'phone',
    std.FULL_NAME: 'Sample Student',
    std.MAJOR: 'major',
    std.SCHOOL_YEAR: 'school_year',
    std.GPA: 'GPA',
    std.SKILL: 'skills'
}


def test_add_student():
    """
    Test adding a student.
    """
    resp = TEST_CLIENT.post(ep.STUDENT_ADD, json=SAMPLE_STUDENT)
    assert std.student_exists(SAMPLE_STUDENT_NM)
    std.del_user(SAMPLE_STUDENT_NM)

def test_get_students_list():
    resp = TEST_CLIENT.get(ep.STUDENT_LIST_W_NS)
    resp_json = resp.get_json()
    assert isinstance(resp_json[ep.STUDENT_LIST_NM], list)

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