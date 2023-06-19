#!/usr/bin/python3
"""This module creates the Base class for our project"""
import json


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize and validate the base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json representation of list_dictionaries"""
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This function writes the json string rep of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                _dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation json_string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a class with the parameters passed"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a json file"""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as f:
                _dicts = Base.from_json_string(f.read())
                return [cls.create(**_dict) for _dict in _dicts]
        except IOError:
            return []
