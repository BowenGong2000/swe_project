"""
This module encapsulates details about students.
"""

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


def get_students():
    return list(students.keys())

def get_students_dict():
    return students


def get_student_details(student):
    return students.get(student, None)


def student_exists(name):
    """
    Returns whether or not the student exists.
    """
    return name in students


def add_student(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    students[name] = details


def get_students_dict():
    return students


def del_students(name):
    del students[name]


def main():
    students = get_students()
    print(f'{students=}')
    print(f'{get_student_details(TEST_STUDENT_NAME)=}')


if __name__ == '__main__':
    main()
