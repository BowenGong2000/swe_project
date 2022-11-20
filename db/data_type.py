"""
This module encapsulates details about data type.
"""

data_types = {
    "Project": {'Name': 'info', 'Requirments': 'info',
                'Start_time': 'time', 'Time_period': 'time',
                'Salary': 'number'},
    "Student": {'Name': 'info', 'Email_address': 'info',
                'Phone_number': 'info', 'Skills': 'info'},
    "Sponsor": {'Name': 'info', 'Email_address': 'info',
                'Phone_number': 'info'}
    }


def add_data_type(type_name, traits):
    if data_type_exists(type_name):
        raise ValueError(f'Data type exists: {type_name=}')
    data_types[type_name] = traits


def del_data_type(type_name):
    if data_type_exists(type_name):
        del data_types[type_name]


def data_type_exists(type_name):
    return type_name in data_types


def get_data_type_dict():
    return data_types


def get_data_types():
    return list(data_types.keys())


def get_data_type_details(data_type):
    return data_types.get(data_type, None)


def main():
    """
    print details of a given data type (dictionary)
    """
    print(data_types["Project"])
    print(get_data_type_details("Project"))

    """
    print a list of data types
    """
    char_types = get_data_types()
    print(char_types)


if __name__ == '__main__':
    main()
