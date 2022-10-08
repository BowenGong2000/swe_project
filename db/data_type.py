"""
This module encapsulates details about data type.
"""

DATA_TYPES = {"Project": {'info': 6},
              "User": {'info': 7},
              "Comment": {'info': 8}, }


def get_data_types():
    return list(DATA_TYPES.keys())


def get_data_type_details(data_type):
    return DATA_TYPES[data_type]


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
