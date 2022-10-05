
import db.dbmongo as mg


def test_init():
    mgs = mg.hello()
    assert isinstance(mgs,list)
