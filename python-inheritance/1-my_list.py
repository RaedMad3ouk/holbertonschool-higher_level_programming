#!/usr/bin/python3
"""inherite from class list"""


class MyList(list):
    """define fields of my class"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
