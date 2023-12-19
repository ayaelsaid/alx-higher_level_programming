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
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
