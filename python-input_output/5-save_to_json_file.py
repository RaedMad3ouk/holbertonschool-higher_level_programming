#!/usr/bin/python3
"""a function that writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """Writes Python obj to file using JSON represenation"""
    import json

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
