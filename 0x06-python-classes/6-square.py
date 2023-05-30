#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initailizes instance of the class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter for size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Get position of square object"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for the object position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """prints a square with the character #"""
        if self.__size <= 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__postion[0] + '#' * self.__size)

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
