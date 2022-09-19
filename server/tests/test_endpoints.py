
import pytest

import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

def test_hello():
    """
    see if Hello works
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)



