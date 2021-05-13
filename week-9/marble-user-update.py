import pymongo
from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)

db = client.web335

db.users.update_one(
    {"employee_id":"8675303"},

    {
        "$set":{
            "email":"fmarble@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id":"8675303"}))