#!/usr/bin/python3
"""Module that converts class attributes to json"""


def class_to_json(obj):
    """returns the dictionary description for JSON serialization"""
    return obj.__dict__
