#!/usr/bin/python3
"""Module that adds new attribute to an object"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to obj is fail, raise TypeError Exception"""
    # checks if the obj object has a __dict__ attribute
    # If the object has __dict__ attr, it means new attr can be added
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
