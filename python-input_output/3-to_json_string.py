#!/usr/bin/python3
"""Contains function that returns JSON representation of object"""


def to_json_string(my_obj):
    """Returns JSON representation"""
    import json

    return json.dumps(my_obj)
