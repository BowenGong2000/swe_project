import pytest

import db.students as std


def test_get_students():
    stds = std.get_students()
    assert isinstance(stds, list)
    assert len(stds) > 1


def test_get_student_details():
    std_dets = std.get_student_details(std.TEST_STUDENT_NAME)
    assert isinstance(std_dets, dict)