"""
This module contains details about projects.
"""
import db.db_connect as dbc

TEST_PROJECT_NAME = 'Test project'
NAME = 'name'
ACCOUNT = 'account'
NUM_MEMBERS = 'num_members'
DEPARTMENT = 'department_name'
MAJOR = 'major_requirements'
SCHOOL_YEAR = 'school_year'
GPA = 'GPA'
LENGTH = 'project_duration'
SKILL = 'skill requirements'
POST_DATE = 'post_date'
DESCRIP = 'description'
APPROVE = "if_approve"
FIELD = 'field'

# We expect the project database to change frequently:
# This list contains our mandatory fields
REQUIRED_FLDS = [ACCOUNT, NUM_MEMBERS, MAJOR, SCHOOL_YEAR, POST_DATE, APPROVE]

PROJECT_KEY = 'name'
PROJECTS_COLLECT = 'projects'


def get_projects():
    dbc.connect_db()
    return dbc.fetch_all(PROJECTS_COLLECT)


def get_project_details(project):
    dbc.connect_db()
    return dbc.fetch_one(PROJECTS_COLLECT, {PROJECT_KEY: project})


def get_projects_dict():
    dbc.connect_db()
    return dbc.fetch_all_as_dict(PROJECT_KEY, PROJECTS_COLLECT)


def del_project(name):
    """
    Delete a doc from db collection by its name.
    """
    return dbc.del_one(PROJECTS_COLLECT, {PROJECT_KEY: name})


def check_if_exist(name):
    """
    check whether or not a project exists.
    """
    return get_project_details(name) is not None


def add_project(name, details):
    doc = details
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')

    if not isinstance(details, dict):
        raise TypeError(f'Wrong type for details: {type(details)=}')

    for field in REQUIRED_FLDS:
        """
        check if missing any data for mandatory fields; if not, raise error
        """
        if field not in details:
            raise ValueError(f'Required {field=} missing from details.')
    dbc.connect_db()
    doc[PROJECT_KEY] = name
    return dbc.insert_one(PROJECTS_COLLECT, doc)


def change_project_single_field(name, field, val):
    if not isinstance(name, str):
        raise TypeError(f'Wrong type for name: {type(name)=}')

    if not isinstance(field, str):
        raise TypeError(f'Wrong type for details: {type(field)=}')
    dbc.connect_db()
    return dbc.change_one(NAME, name, APPROVE, val, PROJECTS_COLLECT)


def main():
    print('Getting projects as a list:')
    projects = get_projects()
    print(f'{projects=}')
    print('Getting projects as a dict:')
    projects = get_projects_dict()
    print(f'{projects=}')
    print(f'{get_project_details(TEST_PROJECT_NAME)=}')


if __name__ == '__main__':
    main()
