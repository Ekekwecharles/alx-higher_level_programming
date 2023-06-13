#!/usr/bin/python3
"""Module that returns JSON rep of an object (string)"""
import json


def to_json_string(my_obj):
    """function that returns JSON rep of an object (string)"""
    return json.dumps(my_obj)
