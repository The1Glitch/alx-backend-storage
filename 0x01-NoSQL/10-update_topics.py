#!/usr/bin/env python3
"""
The function changes all topics of a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    updates many rowa
    """
    return mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
