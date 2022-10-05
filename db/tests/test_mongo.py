
import db.db_mongo as mg

def initial_test():
    mgs = mg.hello()
    assert isinstance(mgs,str)