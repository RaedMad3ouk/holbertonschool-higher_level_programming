#!/usr/bin/python3
"""Define Square class"""


class Square:
    """define fields and methods of Square"""

    def __init__(self, size=0):
        """ Square Constructor.

            args:
               size (int, optional): The size of the square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
