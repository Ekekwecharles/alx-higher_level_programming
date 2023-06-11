#!/usr/bin/python3
"""Module that checks for sub class"""


def inherits_from(obj, a_class):
    """Returns true if type of obj is a subclass of a_class"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
