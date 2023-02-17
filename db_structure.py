import pymongo
import db.projects as pj
import requests

"""
this file is used for checking currently available data.
"""

def curr_data():
    client = pymongo.MongoClient('mongodb+srv://tracyzhu0608:1234@cluster0.8pa03kh.mongodb.net/?retryWrites=true&w=majority', 27017)
    db1 = client.projectdb
    
    result = db1.list_collection_names(session = None)
    print("forms in projectdb:", result)
    for ele in result:
        var = db1[ele].find()
        print(ele, " table")
        for doc in var:
            print(doc)

    db2 = client.user_login_system
    result = db2.list_collection_names(session = None)
    print("forms in user_login_system:", result)
    print("users table")
    var = db2.users.find()
    for doc in var:
        print(doc)
    print(pj.get_projects_dict())


data = requests.get("https://project-finder.herokuapp.com/dict").json()
print(data)