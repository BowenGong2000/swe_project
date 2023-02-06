"""
This module encapsulates details about students.
"""

import db.db_connect as dbc

TEST_STUDENT_NAME = 'Test student'
EMAIL = 'email'
PHONE = 'phone'
FULL_NAME = 'full_name'
MAJOR = 'major'
SCHOOL_YEAR = 'school_year'
GPA = 'GPA'
SKILL = 'skills'

REQUIRED_FLDS = [EMAIL]
students = {TEST_STUDENT_NAME:
            {EMAIL: 'a@nyu.com',
                PHONE: '1111111111',
                FULL_NAME: 'Farry Botter',
                MAJOR: 'Computer Science',
                SCHOOL_YEAR: 'sophomore',
                GPA: 3.5,
                SKILL: 'C++, python'},
            'student_2':
            {EMAIL: 'a@nyu.com',
                PHONE: '1111111111',
                FULL_NAME: 'Farry Botter',
                MAJOR: 'Computer Science',
                SCHOOL_YEAR: 'sophomore',
                GPA: 3.5,
                SKILL: 'C++, python'},
            }

STUDENT_KEY = 'name'
STUDENTS_COLLECT = 'students'


def get_students():
    dbc.connect_db()
    return dbc.fetch_all(STUDENTS_COLLECT)


def get_students_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(STUDENT_KEY, STUDENTS_COLLECT)


def get_student_details(student):
    dbc.connect_db()
    return dbc.fetch_one(STUDENTS_COLLECT, {STUDENT_KEY: student})


def student_exists(name):
    """
    check whether or not a student exists.
    """
    return get_student_details(name) is not None


def add_student(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')

    """
    check if missing any data for mandatory fields; if not, raise error
    """
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')

    doc = details
    """
    insert the student to db
    """
    dbc.connect_db()
    doc[STUDENT_KEY] = name
    return dbc.insert_one(STUDENTS_COLLECT, doc)


def del_student(name):
    """
    Delete a doc from db collection by its name.
    """
    return dbc.del_one(STUDENTS_COLLECT, {STUDENT_KEY: name})


def main():
    students = get_students()
    print(f'{students=}')
    print(f'{get_student_details(TEST_STUDENT_NAME)=}')


if __name__ == '__main__':
    main()
