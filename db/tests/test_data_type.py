import pytest

import db.data_type as dtyp

TEST_DATA_TYPE = "Project"

NEW_DATA_TYPE = 'Student'
DEF_TRAITS = {'email': 'xxx@nyu.edu', 'phone': 'xxxxxxxx'}

def test_get_data_types():
    assert isinstance(dtyp.get_data_types(), list)

def test_get_data_type_details():
    details = dtyp.get_data_type_details(TEST_DATA_TYPE)
    assert isinstance(details, dict)


def test_add_data_type():
    assert dtyp.data_type_exists(NEW_DATA_TYPE)


def test_add_data_type_dup():
    with pytest.raises(ValueError):
        dtyp.add_data_type(NEW_DATA_TYPE, DEF_TRAITS)


def test_data_type_exists():
    assert dtyp.data_type_exists(NEW_DATA_TYPE)


def test_data_type_not_exists():
    assert not dtyp.data_type_exists('Some nonsense data type')