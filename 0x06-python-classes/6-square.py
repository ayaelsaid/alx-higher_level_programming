#!/usr/bin/python3
"""
without importing any module
"""


class Square:
    """
    Empty class that define a square by Private instance attribute size,
    instantiation with size
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        size : no type/value verification
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

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

    @property
    def position(self):
        """
        retrieve it
        """
        return self.__position

    def position(self, value):
        """
        set it
        """
        if (
                type(value) is not tuple or
                type(value[0]) is not int or
                type(value[1]) is not int or
                value[0] < 0 or
                value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
