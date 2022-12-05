import pytest
import os
import db.students as std

RUNNING_ON_CICD_SERVER = os.environ.get('CI', False)


def test_get_students():
    stds = std.get_students()
    assert isinstance(stds, list)
    assert len(stds) > 1


def test_get_student_details():
    std_dets = std.get_student_details(std.TEST_STUDENT_NAME)
    assert isinstance(std_dets, dict)


def test_add_student():
    details = {}
    for field in std.REQUIRED_FLDS:
        details[field] = 2
    std.add_student(std.TEST_STUDENT_NAME, details)
    assert std.student_exists(std.TEST_STUDENT_NAME)


def test_add_wrong_name_type():
    with pytest.raises(TypeError):
        std.add_student(7, {})


def test_add_wrong_details_type():
    with pytest.raises(TypeError):
        std.add_student('a new student', [])


def test_add_missing_field():
    with pytest.raises(ValueError):
        std.add_student('a new student', {'foo': 'bar'})


def test_get_students_dict():
    if not RUNNING_ON_CICD_SERVER:
        stds = std.get_students_dict()
        assert isinstance(stds, dict)
        assert len(stds) > 1