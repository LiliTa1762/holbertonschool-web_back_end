#!/usr/bin/env python3
"""List all docs in collection"""

def list_all(mongo_collection):
    """ List all documents in Python"""
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
