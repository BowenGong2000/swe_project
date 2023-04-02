"""
This module contains details about sponsors.
"""

TEST_SPONSOR_NAME = 'Test sponsor'
NAME = 'name'
DEPARTMENT = 'department_name'
EMAIL = 'email'
PHONE = 'phone'

REQUIRED_FLDS = [EMAIL]
sponsors = {TEST_SPONSOR_NAME:
            {DEPARTMENT: 'computer_engineering',
                EMAIL: '12345@nyu.edu',
                PHONE: '1111111'},
            'sponsor_2':
            {DEPARTMENT: 'computer_engineering',
                EMAIL: '12345@nyu.edu',
                PHONE: '222222'},
            }


def get_sponsors():
    return list(sponsors.keys())


def get_sponsors_dict():
    return sponsors


def get_sponsor_details(sponsor):
    return sponsors.get(sponsor, None)


def del_sponsor(name):
    del sponsors[name]


def sponsor_exists(name):
    """
    check whether or not a sponsor name exists.
    """
    return name in sponsors


def add_sponsor(name, details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')
    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')
    for field in REQUIRED_FLDS:
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    sponsors[name] = details


def main():
    sponsors = get_sponsors()
    print(f'{sponsors=}')
    print(f'{get_sponsor_details(TEST_SPONSOR_NAME)=}')


if __name__ == '__main__':
    main()
