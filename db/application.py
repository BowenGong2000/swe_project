"""
This module contains details about application.
"""
import db.db_connect as dbc

TEST_APPLICATION_NAME = 'Test application'
NAME = 'application_name'
APPLICANT_NAME = 'applicant_name'
APPLICANT_EMAIL = 'applicant_email'
PROJECT = 'applied_project'
APP_DATE = 'application_date'
APP_STATUS = 'application_status'
RESUME_FILENAME = 'resume_filename'
RESUME_CONTENT = 'resume_content'
TRANSCRIPT_FILENAME = 'transcript_filename'
TRANSCRIPT_CONTENT = 'transcript_content'
COVERLETTER_FILENAME = 'coverleter_filename'
COVERLETTER_CONTENT = 'coverletter_content'

REQUIRED_FLDS = [NAME, APPLICANT_EMAIL, PROJECT, APP_DATE,
                 RESUME_FILENAME, RESUME_CONTENT]

APPLICATION_COLLECT = 'applications'
APPLICATION_KEY = 'application_name'


def get_applications():
    dbc.connect_db()
    return dbc.fetch_all(APPLICATION_COLLECT)


def get_applications_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict('applicant_email', APPLICATION_COLLECT)


def get_application_details(name):
    dbc.connect_db()
    return dbc.fetch_one(APPLICATION_COLLECT, {'application_name': name})


def get_user_application(user_email):
    dbc.connect_db()
    return dbc.fetch_all_with_filt(APPLICATION_COLLECT,
                                   {'applicant_email': user_email})


def get_project_application(project):
    dbc.connect_db()
    return dbc.fetch_all_with_filt(APPLICATION_COLLECT,
                                   {'applied_project': project})


def application_exists(name):
    """
    check whether or not a application exists.
    """
    return get_application_details(name) is not None


def del_application(name):
    """
    Delete a doc from db collection by its name.
    """
    return dbc.del_one(APPLICATION_COLLECT, {APPLICATION_KEY: name})


def add_application(name, appl_details):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')

    if not isinstance(appl_details, dict):
        raise TypeError(f'Wrong type for details: {type(appl_details)=}')

    for field in REQUIRED_FLDS:
        """
        check if missing any data for mandatory fields; if not, raise error
        """
        if field not in appl_details:
            raise ValueError(f'Required {field=} missing from details.')
    dbc.connect_db()
    appl_details[APPLICATION_KEY] = name
    return dbc.insert_one(APPLICATION_COLLECT, appl_details)


def get_application_num():
    dbc.connect_db()
    count = dbc.counter(APPLICATION_COLLECT)
    if count:
        return count
    return None


def main():
    applications = get_applications()
    print(f'{applications=}')
    print(f'{get_application_details(TEST_APPLICATION_NAME)=}')


if __name__ == '__main__':
    main()
