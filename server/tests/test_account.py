
import server.validation_methods as md


def test_User_Validation():
    """
    Check if user info are valid
    """
    test_user = {
    "name": "Mark",
    "email": "yw4111@nyu.edu",
    "phone": "6467248912",
    "password": "Mark0445!"
    }
    testres = md.User_Validation(test_user)
    assert testres
