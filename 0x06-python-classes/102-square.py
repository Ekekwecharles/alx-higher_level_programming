#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initailizes instance of the class"""
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __gt__(self, other):
        return self.area() > other.area()
