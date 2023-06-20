#!/usr/bin/python3
"""This module creates the Base class for our project"""
import json
import csv


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in csv"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in csv"""
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                _dicts = csv.DictReader(f, fieldnames=fields)
                _dicts = [dict([k, int(v)] for k, v in d.items())
                          for d in _dicts]
                return [cls.create(**d) for d in _dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """drawing shapes
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        # adding color
        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()  # hide turtle

        # exit when cliked
        turtle.exitonclick()
