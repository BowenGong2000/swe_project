"""
This module encapsulates details about posted contenton web.
"""

TEST_CONTENT_NAME = 'Test content'
EMAIL = 'email'
PHONE = 'phone'
FULL_NAME = 'full_name'
TAG = 'tag'
PROJ_NAME = 'proj_name'
CONTENT = 'content'

REQUIRED_FLDS = [EMAIL]
contents = {TEST_CONTENT_NAME:
            {EMAIL: 'a@nyu.com',
                PHONE: '1111111111',
                FULL_NAME: 'Farry Botter',
                TAG: 'Computer Science',
                PROJ_NAME: 'Simple Web Design',
                CONTENT: 'This project is design for web design'},
            'content_2':
            {EMAIL: 'a@nyu.com',
                PHONE: '1111111111',
                FULL_NAME: 'Farry Botter',
                TAG: 'Civil Engineering',
                PROJ_NAME: 'Torrnado Destruction Prediction',
                CONTENT: 'Project will predict destruction rate of torrnado'}
            }


def get_proj():
    return list(contents.keys())


def get_contents_dict():
    return contents


def get_content_details(content):
    return contents.get(content, None)


def content_exists(name):
    """
    Returns whether or not the student publish content.
    """
    return name in contents


def add_student(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    contents[name] = details


def del_contents(name):
    del contents[name]


def main():
    students = get_proj()
    print(f'{students=}')
    print(f'{get_content_details(TEST_CONTENT_NAME)=}')


if __name__ == '__main__':
    main()
