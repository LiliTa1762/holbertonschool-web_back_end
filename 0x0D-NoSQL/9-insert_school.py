#!/usr/bin/env python3
"""Insert based on kwargs"""

def insert_school(mongo_collection, **kwargs):
    """ Insert a document in Python"""
    x = mongo_collection.insert_one(kwargs)
    return (x.inserted_id)
