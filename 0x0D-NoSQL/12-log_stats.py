#!/usr/bin/env python3
"""Stats about Ngnix logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    log = client.logs.nginx
    all = log.count_documents({})
    print(all, "logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = log.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    check_get = log.count_documents(
        {'method': 'GET', 'path': "/status"})
    print(f"{check_get} status check")
