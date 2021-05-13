import pymongo
from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user={
    "first_name": "Jean",

    "last_name": "Van Dam",

    "email": "jvandam@mail.com",

    "employee_id": "8675303",

    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id":"8675303"}))

pprint.pprint(db.users.find_one())