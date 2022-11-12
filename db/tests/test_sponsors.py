import db.sponsors as sp


def test_get_sponsors():
    sps = sp.get_sponsors()
    assert isinstance(sps, list)
    assert len(sps) > 1


def test_get_sponsor_details():
    sp_dets = sp.get_sponsor_details(sp.TEST_SPONSOR_NAME)
    assert isinstance(sp_dets, dict)


def test_get_sponsors_dict():
    sps = sp.get_sponsors_dict()
    assert isinstance(sps, dict)
    assert len(sps) > 1


def test_add_sponsor():
    details = {}
    for field in sp.REQUIRED_FLDS:
        details[field] = 2
    sp.add_sponsor(sp.TEST_SPONSOR_NAME, details)
    assert sp.sponsor_exists(sp.TEST_SPONSOR_NAME)