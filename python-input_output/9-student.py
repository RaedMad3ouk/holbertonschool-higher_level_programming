#!/usr/bin/python3
"""
Contains class Student
that initializes public instance attributes first_name, last_name, and age,
"""


class Student():
    """
    Public Attributes:
        first_name
        last_name
        age
        """

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary description with simple data structure"""
        return self.__dict__
