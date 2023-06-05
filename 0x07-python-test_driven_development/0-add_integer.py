#!/usr/bin/python3
"""Addition moodule"""


def add_integer(a, b=98):
    """Adds two integers"""
    # if not isinstance(a, (int, float)):
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    # if not isinstance(b, (int, float)):
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
