"""
This module contains details about projects.
"""

TEST_PROJECT_NAME = 'Test project'
NUM_MEMBERS = 'num_members'

# We expect the project database to change frequently:
projects = {TEST_PROJECT_NAME: 
            {NUM_MEMBERS: 7, 'Skill_requirement': 'math'},
'project2': {NUM_MEMBERS: 9, 'Skill_requirement': 'computer_science'},
'project3': {NUM_MEMBERS: 6, 'Skill_requirement': 'design'}, 
            }


def get_projects():
    return list(projects.keys())


def get_project_details(project):
    return projects.get(project, None)


def main():
    projects = get_projects()
    print(f'{projects=}')
    print(f'{get_project_details(TEST_PROJECT_NAME)=}')


if __name__ == '__main__':
    main()
