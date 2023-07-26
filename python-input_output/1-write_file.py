#!/usr/bin/python3
"""writes a string to a text file and returns the number of chars written"""


def write_file(filename="", text=""):
    """writes to text file and returns num chars written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
