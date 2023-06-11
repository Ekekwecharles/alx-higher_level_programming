#!/usr/bin/python3
"""This module defines a Square class and inherits from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """Inializes obj of the class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
