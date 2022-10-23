
import pytest

import server.models as md


User = {
    "name": "Mark",
    "email": "yw4111@nyu.edu",
    "phone": "6467248912",
    "password": "Mark0445!"
}


def test_User_Validation():
    """
    Check if user info are valid
    """
    test_res = md.User_Validation(User)
    assert test_res == True
