#!/usr/bin/python3
"""Bytecode"""
import math


class MagicClass:
    """Class"""

    def __init__(self, radius=0):
        """initializer"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.___radius = radius

    def area(self):
        """area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """circum"""
        return 2 * math.pi * self.__radius
