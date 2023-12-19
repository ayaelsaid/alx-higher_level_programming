#!/usr/bin/python3
"""
without importing any module
"""


class Square:
    """
    Empty class that define a square by Private instance attribute size,
    instantiation with size
    """
    def __init__(self, size=0):
        """
        size : no type/value verification
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Public instance that returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        retrieve instance attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set instance attribute
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
