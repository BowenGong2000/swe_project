import db.sponsors as sp


def test_get_sponsors():
    sps = sp.get_sponsors()
    assert isinstance(sps, list)
    assert len(sps) > 1


def test_get_sponsor_details():
    sp_dets = sp.get_sponsor_details(sp.TEST_SPONSOR_NAME)
    assert isinstance(sp_dets, dict)
