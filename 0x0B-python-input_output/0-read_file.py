#!/usr/bin/python3
"""Module that reads a text file"""


def read_file(filename=""):
    """Function that reads from a file"""
    with open(filename, encoding="utf-8") as f:
        for file in f:
            print(file, end="")
