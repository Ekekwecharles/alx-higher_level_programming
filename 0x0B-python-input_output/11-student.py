#!/usr/bin/python3
"""Module that defines a class"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """Initialize object of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if (type(attrs) == list and all(type(s) == str for s in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__i

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
