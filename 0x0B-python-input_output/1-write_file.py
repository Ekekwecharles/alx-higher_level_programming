#!/usr/bin/python3
"""Module that writes to a file"""


def write_file(filename="", text=""):
    """Function that writes to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
