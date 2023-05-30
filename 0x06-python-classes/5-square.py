#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initailizes instance of the class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
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

    def my_print(self):
        """prints a square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
