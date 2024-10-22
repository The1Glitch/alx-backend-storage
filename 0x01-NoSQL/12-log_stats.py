#!/usr/bin/env python3
"""
The function provides some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as the example
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with the number of documents with:
method=GET
path=/status
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Prototype: def log_stats(mongo_collection, option=None):
    Provide some stats about Nginx logs stored in MongoDB
    """
    items = {}
    if option:
        value = mongo_collection.count_document(
                {"method": {"$regex": option}})
        print(f"\method {option}: {value}")
        return

    result = mongo_collection.count_document(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_document({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://102.66.208.183').logs.nginx
    log_stats(nginx_collection)
