#!/usr/bin/env python3
"""inserts new document in collection based on kwargs"""


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """inserts new document in collection based on kwargs"""

    my_dict = {}
    for key, value in kwargs.items():
        my_dict[key] = value
    result = mongo_collection.insert_one(my_dict)
    return result.inserted_id
