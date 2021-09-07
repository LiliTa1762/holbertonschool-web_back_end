#!/usr/bin/env python3
""" Return the list of collection having a topic"""

def schools_by_topic(mongo_collection, topic):
    """Return list of school with a topic"""
    return mongo_collection.find({"topics": topic})
