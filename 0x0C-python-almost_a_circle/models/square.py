#!/usr/bin/python3
"""This module defines a square class that inherits from a
Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize an Object of the square class, in this case
        width = height = size because it's a square"""
        width = height = size
        super().__init__(width, height, x, y, id)

    @property
    def size(self):
        """Getter function for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter function for size which in turn change width and height
        When you call width and height without the underscore, the setter
        and getters of the attr will be invoked from Rectangle
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the parameters of Object with values from args"""
        attr = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, v in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], v)
        else:
            for k, v in kwargs.items():
                if k in attr:
                    setattr(self, k, v)

    def __str__(self):
        """Return a string rep of the class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """Returns the dictionary representation of the Square class"""
        _dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return _dict
