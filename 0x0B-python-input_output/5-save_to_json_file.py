#!/usr/bin/python3
"""Module that writes an Obj to a text file, using a JSON rep"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Obj to a text file, using a JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
