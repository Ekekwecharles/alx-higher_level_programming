#!/usr/bin/python3
"""BaseGeometry Module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area of geometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value parameter"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
