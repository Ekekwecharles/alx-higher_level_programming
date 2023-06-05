#!/usr/bin/python3
"""Print Square module"""


def print_square(size):
    """print a square with '#' of size 'size'"""
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
