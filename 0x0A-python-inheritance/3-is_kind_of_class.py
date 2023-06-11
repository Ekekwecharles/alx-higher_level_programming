#!/usr/bin/python3
"""Module that checks if an object is an instance of a class of its
super classes"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its super
    classes else False"""
    return isinstance(obj, a_class)
