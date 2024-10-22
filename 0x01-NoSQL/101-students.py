#!/usr/bin/env python3
"""
Py function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """ Student by score """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "avarageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "avarageScore": -1
                }
        }
    ])
