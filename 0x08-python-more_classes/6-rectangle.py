#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Defines an empty class"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Intializes instance of the class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates and returns the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Validates the input and return the perimeter of a rect"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def print(self):
        """Prints the rectange with the character '#'"""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        for _ in range(self.__height):
            result += "#" * self.__width + "\n"
        return result[:-1]

    def __str__(self):
        """prints a string representation of the object"""
        return self.print()

    def __repr__(self):
        """Returns a representation of how the function can be used"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a custom message when an object is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
