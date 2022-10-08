import db.data_type as dtyp
TEST_DATA_TYPE = "Project"

def test_get_data_types():
    assert isinstance(dtyp.get_data_types(), list)

def test_get_data_type_details():
    details = dtyp.get_data_type_details(TEST_DATA_TYPE)
    assert isinstance(details, dict)