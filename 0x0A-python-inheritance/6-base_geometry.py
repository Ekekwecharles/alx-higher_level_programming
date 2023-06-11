#!/usr/bin/python3
"""Module that raises an exception"""


class BaseGeometry:
    """Class that raises an exception"""
    def area(self):
        """raise an Execiption"""
        raise Exception('area() is not implemented')
