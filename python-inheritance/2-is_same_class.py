#!/usr/bin/python3
"""2is_same_class"""


def is_same_class(obj, a_class):
    """return True if the object is exactly an instance of a class"""
    if type(obj) == a_class:
        return True
    else:
        return False
hah