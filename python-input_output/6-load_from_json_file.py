#!/usr/bin/python3
"""Contains function that creates a Python obj from JSON file"""


def load_from_json_file(filename):
    """Creates a Python obj from JSON file"""
    import json

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
