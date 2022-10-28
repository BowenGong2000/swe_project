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


def get_sponsor_details(sponsor):
    return sponsors.get(sponsor, None)


def del_sponsor(name):
    del sponsors[name]


def get_sponsors_dict():
    return sponsors


def check_if_exist(name):
    """
    check whether or not a sponsor name exists.
    """
    return name in sponsors


def main():
    sponsors = get_sponsors()
    print(f'{sponsors=}')
    print(f'{get_sponsor_details(TEST_SPONSOR_NAME)=}')


if __name__ == '__main__':
    main()
