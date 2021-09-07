#!/usr/bin/env python3
"""Stats about Ngnix logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')	
    log = client.logs.nginx
    all = log.count_documents({})
    print(all, "logs")

    print("Methods:")
    print("method GET:", log.count_documents({"method": "GET"}))
    print("method POST:", log.count_documents({"method": "POST"}))
    print("method PUT:", log.count_documents({"method": "PUT"}))
    print("method PATCH:", log.count_documents({"method": "PATCH"}))
    print("method DELETE:", log.count_documents({"method": "DELETE"}))

    print(log.count_documents({"path": "/status"}), "status check")

