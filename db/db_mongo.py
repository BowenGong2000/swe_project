"""
#todo
"""
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://tracyzhu0608:1234"
    "@cluster0.8pa03kh.mongodb.net/?re"
    "tryWrites=true&w=majority"
    )
db = cluster["test"]
collection = db["test"]

post1 = {"_id": 0, "project name": "chatbot", "start date": "2023-5-1"}
post2 = {"_id": 1, "project name": "chatbot1", "start date": "2023-5-1"}
post3 = {"_id": 2, "project name": "chatbot2", "start date": "2023-5-1"}

# collection.insert_one(post1)
# collection.insert_many([post2, post3])

# collection.delete_many()

collection.update_one({"_id": 0}, {"$set": {"project name": "Chatbot"}})
collection.update_one({"_id": 0}, {"$set": {"instructor": "Tim"}})

results = collection.find({})
for x in results:
    print(x)

post_count = collection.count_documents({})
print(post_count)
