"""
This module contains all methods to interact with the PROJECT_DB.
"""
import os
import pymongo as pm
import gridfs

CLOUD = "1"
LOCAL = "0"
PROJECT_DB = 'projectdb'
client = None


def connect_db():
    """
    This provides a uniform way to connect to the DB across all uses.
    """
    global client
    if client is None:  # not connected yet!
        print("Setting client because it is None.")
        if os.environ.get("CLOUD_MONGO", CLOUD) == CLOUD:
            password = os.environ.get('MONGO_PW')
            if not password:
                print("password=",password)
                raise ValueError('You must set your password '
                                 + 'to use Mongo in the cloud.')

            client = pm.MongoClient(f'mongodb+srv://tracyzhu0608:{password}'
                                    + '@cluster0.8pa03kh.mongodb.net/'
                                    + '?retryWrites=true&w=majority', 27017)

            print("Connecting to Mongo in the cloud.")

        else:
            print("Connecting to Mongo locally.")
            client = pm.MongoClient()


def insert_one(collection, doc, db=PROJECT_DB):
    """
    Insert a single doc into collection.
    """
    print(f'{db=}')
    return client[db][collection].insert_one(doc)


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
        del doc['_id']
        return doc


def fetch_all_with_filt(collection, filt, db=PROJECT_DB):
    """
    Find with a filter and return all doc found.
    """
    ret = []
    for doc in client[db][collection].find(filt):
        del doc['_id']
        ret.append(doc)
    return ret


def fetch_all(collection, db=PROJECT_DB):
    """
    Find all docs within the DB and reuturn in list
    """
    ret = []
    for doc in client[db][collection].find():
        del doc['_id']
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


def change_one(key_field, key, field, val, collection, db=PROJECT_DB):
    """
    Change value in a field
    """
    ret = None
    mod_key = {key_field: key}
    for doc in client[db][collection].find():
        if doc['name'] == key:
            ret = doc
    if ret:
        ret[field] = val
        client[db][collection].replace_one(mod_key, ret)
    return ret


def insert_file(name, filename, file, db=PROJECT_DB):
    """
    insert a file in to db
    """
    data = file.read()
    fs = gridfs.GridFS(client[db])
    return fs.put(data, filename=filename, name=name)


def delete_file(info_dict, db=PROJECT_DB):
    """
    delete a file in db
    """
    fs = gridfs.GridFS(client[db])
    file_id = fs.find_one(info_dict)._id
    return fs.delete(file_id)


def check_file(info_dict, db=PROJECT_DB):
    """
    check if file exist
    """
    fs = gridfs.GridFS(client[db])
    if fs.find_one(info_dict) is not None:
        return True
    return False


def get_file(info_dict, db=PROJECT_DB):
    """
    get a existing file
    """
    fs = gridfs.GridFS(client[db])
    if fs.find_one(info_dict) is not None:
        file = fs.find_one(info_dict)
        return file, file.filename
    else:
        return None, None


def insert_pic(email, filename, file, db=PROJECT_DB):
    """
    insert a picture with email as key
    """
    data = file.read()
    fs = gridfs.GridFS(client[db])
    return fs.put(data, email=email, filename=filename)


def counter(collection, db=PROJECT_DB):
    """
    count the total number of collection
    """
    ret = client[db][collection].count_documents({})
    if ret:
        return ret
    return None


def main():
    connect_db()


if __name__ == '__main__':
    main()
