#!/usr/bin/python3
"""defie a methode is_same_class"""


def inherits_from(obj, a_class):
    """returns true if object is an instance of the given class.

    arguments:
    obj: object that will be checked
    a_class:the class that willbe compared with obj type
    """
    if type(obj) == a_class:
        return False
    else:
        if isinstance(obj, a_class):
            return True
        else:
            return False
