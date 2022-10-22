"""
This module encapsulates details about students.
"""

TEST_STUDENT_NAME = 'Test student'
EMAIL = 'email'
PHONE = 'phone'
FULL_NAME = 'full_name'

REQUIRED_FLDS = [EMAIL]
students = {TEST_STUDENT_NAME:
            {EMAIL: 'a@nyu.com',
                PHONE: '1111111111',
                FULL_NAME: 'Farry Botter'},
            'student2':
            {EMAIL: 'b@nyu.com',
                PHONE: '2222222222',
                FULL_NAME: 'Pruce Rayne'}
            }


def get_students():
    return list(students.keys())


def get_student_details(student):
    return students.get(student, None)


def main():
    students = get_students()
    print(f'{students=}')
    print(f'{get_student_details(TEST_STUDENT_NAME)=}')


if __name__ == '__main__':
    main()
