#!/usr/bin/python3
"""This module inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initializes objects of the rctanglr class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the Rectangle object"""
        s = "[" + str(self.__class__.__name__) + "] "
        s += str(self.__width) + "/" + str(self.__height)
        return s
