
import server.validation_methods as md


def test_user_validation():
    """
    Check if user info are valid
    """
    test_user = {
    "name": "Mark123",
    "email": "yw4111@nyu.edu",
    "phone": "6467248912",
    "password": "Mark0445!"
    }
    testres = md.User_Validation(test_user)
    assert testres


def test_postlength_validataion():
    """
    check if posted info is in correct format
    """
    test_case = "project discription"
    return md.Postlength_Validataion(test_case)
