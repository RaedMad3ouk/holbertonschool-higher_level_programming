#!/usr/bin/python3
"""
Contains method is_kind_of_class
returns True if object is an instance of class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    args:
    obj: the object to be checked
        a_class:the class that willbe compared with
    Returns:
        if type of obj equal to a_class or inherits from it True
        otherwise false
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
