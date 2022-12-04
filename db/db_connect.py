import os

import pymongo as pm

REMOTE = "0"
LOCAL = "1"

PROJECT_DB = 'projectdb'

client = None


def connect_db():
    """
    This provides a uniform way to connect to the DB across all uses.
    """
    global client
    if client is None:  # not connected yet!
        print("Setting client because it is None.")
        if os.environ.get("LOCAL_MONGO", LOCAL) == LOCAL:
            print("Connecting to Mongo locally.")
            client = pm.MongoClient()


def fetch_all(collection, db=PROJECT_DB):
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_all_as_dict(key, collection, db=PROJECT_DB):
    ret = {}
    for doc in client[db][collection].find():
        del doc['_id']
        ret[doc[key]] = doc
    return ret