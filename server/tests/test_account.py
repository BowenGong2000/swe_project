
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


def test_user_type():
    """
    check if User_type correctly get valid output
    """
    test_user = {
    "name": "Mark123",
    "email": "yw4111@nyu.edu",
    "phone": "6467248912",
    "password": "Mark0445!",
    "type": "3",
    "setting": {"color":1, "subscription": 0}
    }
    return md.User_type(test_user) in [0,1]


def test_setting_type():
    """
    check if Setting_type correctly get valid output
    """
    test_user = {
    "name": "Mark123",
    "email": "yw4111@nyu.edu",
    "phone": "6467248912",
    "password": "Mark0445!",
    "type": "3",
    "setting": {"color":1, "subscription": 0}
    }
    color, subscription = md.Setting_type(test_user)
    ret = color in [0,1,2,3,4] and subscription in [0,1]
    return ret


def account_validation():
    test_user = ['yw4177@nyu.edu', '1806']
    test_manager = ['sc7730@nyu.edu', '1806']
    return md.account_validation(test_user[0], test_user[1]) == 1
