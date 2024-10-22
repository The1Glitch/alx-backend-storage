#!/usr/bin/env python3
"""
This function python lits all documents in collection
"""
import pymongo


def list_all(mongo_collection):
    """
    lists all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
