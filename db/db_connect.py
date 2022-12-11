"""
This module contains all methods to interact with the PROJECT_DB.
"""
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


def insert_one(collection, doc, db=PROJECT_DB):
    """
    Insert a single doc into collection.
    """
    client[db][collection].insert_one(doc)


def del_one(collection, filt, db=PROJECT_DB):
    """
    Delete a single doc from collection with a filter.
    """
    client[db][collection].delete_one(filt)


def fetch_one(collection, filt, db=PROJECT_DB):
    """
    Find with a filter and return on the first doc found.
    """
    for doc in client[db][collection].find(filt):
        return doc


def fetch_all(collection, db=PROJECT_DB):
    """
    Find all docs within the DB and reuturn in list
    """
    ret = []
    for doc in client[db][collection].find():
        ret.append(doc)
    return ret


def fetch_all_as_dict(key, collection, db=PROJECT_DB):
    """
    Find all docs and reuturn in dict {key : name}
    """
    ret = {}
    for doc in client[db][collection].find():
        del doc['_id']
        ret[doc[key]] = doc
    return ret
