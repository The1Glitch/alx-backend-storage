#!/usr/bin/env python3
"""
The function returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find by topic
    """
    return mongo_collection.find({"topics": topic})
