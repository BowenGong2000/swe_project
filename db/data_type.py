"""
This module encapsulates details about data type.
"""

DATA_TYPES = {
    "Project": {'Name': 'info', 'Requirments': 'info',
                'Start_time': 'time', 'Time_period': 'time',
                'Salary': 'number'},
    "Student": {'Name': 'info', 'Email_address': 'info',
                 'Phone_number': 'info', 'Skills': 'info'},
    "Sponor": {'Name': 'info', 'Email_address': 'info',
               'Phone_number': 'info'}
    }


def get_data_types():
    return list(DATA_TYPES.keys())


def get_data_type_details(data_type):
    return DATA_TYPES.get(data_type, None)


def main():
    """
    print details of a given data type (dictionary)
    """
    print(DATA_TYPES["Project"])
    print(get_data_type_details("Project"))

    """
    print a list of data types
    """
    char_types = get_data_types()
    print(char_types)


if __name__ == '__main__':
    main()
