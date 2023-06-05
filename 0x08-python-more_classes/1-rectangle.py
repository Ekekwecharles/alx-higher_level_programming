#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Defines an empty class"""
    def __init__(self, width=0, height=0):
        """Intializes instance of the class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validates and sets the width value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates and sets the height value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
