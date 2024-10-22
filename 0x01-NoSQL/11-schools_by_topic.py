#!/usr/bin/env python3
"""
The function returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    find by topic
    """
    return mongo_collection.find({"topic": topic})
