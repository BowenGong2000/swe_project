
import db.dbmongo as mg


def initial_test():
    mgs = mg.hello()
    assert isinstance(mgs,list)
