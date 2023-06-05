#!/usr/bin/python3
"""A module that prints first name and last name"""


def say_my_name(first_name, last_name=""):
    """Prints Full name of persons"""
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")
