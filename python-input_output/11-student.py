#!/usr/bin/python3
"""define class student"""


class Student:
    """define student"""

    def __init__(self, first_name, last_name, age):
        """class construtor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list and attrs is not None:
            return {attr: getattr(
                self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
