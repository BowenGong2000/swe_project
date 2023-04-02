"""
This module contains details about users.
"""
import db.db_connect as dbc

TEST_USER_EMAIL = 'Test'
NAME = 'name'
EMAIL = 'email'
PHONE = 'phone'
PW = 'password'

REQUIRED_FLDS = [PW]

USER_KEY = 'email'
USER_COLLECT = 'users'


def get_users():
    dbc.connect_db()
    return dbc.fetch_all(USER_COLLECT)


def get_users_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(USER_KEY, USER_COLLECT)


def get_user_details(email):
    dbc.connect_db()
    return dbc.fetch_one(USER_COLLECT, {USER_KEY: email})


def user_exists(email):
    """
    check whether or not a user exists.
    """
    return get_user_details(email) is not None


def get_user_password(email):
    """
    return user registered passwrod in db
    """
    user = get_user_details(email)
    pw = user['password']
    return pw


def del_user(email):
    """
    Delete a doc from db collection by its name.
    """
    return dbc.del_one(USER_COLLECT, {USER_KEY: email})


def add_user(email, usr_details):
    if not isinstance(email, str):
        raise TypeError(f'Wrong type for name: {type(email)=}')

    if not isinstance(usr_details, dict):
        raise TypeError(f'Wrong type for details: {type(usr_details)=}')

    for field in REQUIRED_FLDS:
        """
        check if missing any data for mandatory fields; if not, raise error
        """
        if field not in usr_details:
            raise ValueError(f'Required {field=} missing from details.')
    dbc.connect_db()
    usr_details[USER_KEY] = email
    return dbc.insert_one(USER_COLLECT, usr_details)


def get_user_num():
    dbc.connect_db()
    count = dbc.counter(USER_COLLECT)
    if count:
        return count
    return None


def main():
    users = get_users()
    print(f'{users=}')
    print(f'{get_user_details(TEST_USER_EMAIL)=}')


if __name__ == '__main__':
    main()
