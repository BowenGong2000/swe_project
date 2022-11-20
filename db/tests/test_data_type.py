import pytest

import db.data_type as dtyp

NEW_DATA_TYPE = 'Student_in_waitlist'
DEF_TRAITS = {'email': 'xxx@nyu.edu', 'phone': 'xxxxxxxx'}


@pytest.fixture(scope='function')
def new_data_type():
    dtyp.add_data_type(NEW_DATA_TYPE, DEF_TRAITS)
    yield
    dtyp.del_data_type(NEW_DATA_TYPE)


def test_get_data_type_details(new_data_type):
    details = dtyp.get_data_type_details(NEW_DATA_TYPE)
    assert isinstance(details, dict)


def test_get_data_types():
    assert isinstance(dtyp.get_data_types(), list)
    assert len(dtyp.get_data_types()) > 1


def test_add_data_type(new_data_type):
    assert dtyp.data_type_exists(NEW_DATA_TYPE)


def test_add_data_type_dup(new_data_type):
    with pytest.raises(ValueError):
        dtyp.add_data_type(NEW_DATA_TYPE, DEF_TRAITS)


def test_data_type_exists(new_data_type):
    assert dtyp.data_type_exists(NEW_DATA_TYPE)


def test_data_type_not_exists():
    assert not dtyp.data_type_exists('Some nonsense data type')


@pytest.mark.skip("Can't run this test until the delete function is written.")
def test_del_data_type():
    assert False