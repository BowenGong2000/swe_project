import pytest
import server.endpoints as ep

TEST_CLIENT = ep.app.test_client()

def test_hello():
    """
    see if Hello works
    """
    resp_json = TEST_CLIENT.get(ep.HELLO).get_json()
    assert isinstance(resp_json[ep.MESSAGE], str)

def test_get_DataList():
    """
    see if we can get data list properly
    Return should look like:
        {DATA_LIST_NM: [list of data ...]}
    """
    resp_json = TEST_CLIENT.get(ep.DATA_LIST).get_json()
    assert isinstance(resp_json[ep.DATA_LIST_NM], list)

def test_get_DataList_not_empty():
    """
    see if we can get data list properly
    Return should look like:
        {DATA_LIST_NM: [list of data ...]}
    """
    resp_json = TEST_CLIENT.get(ep.DATA_LIST).get_json()
    assert len(resp_json[ep.DATA_LIST_NM]) > 0

