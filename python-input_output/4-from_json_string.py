#!/usr/bin/python3
"""a function that returns python data structure from JSON string"""


def from_json_string(my_str):
    """Returns python data structure from JSON string"""
    import json

    return json.loads(my_str)
