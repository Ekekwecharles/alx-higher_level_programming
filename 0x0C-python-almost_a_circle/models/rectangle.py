#!/usr/bin/python3
"""This module creates a Rectangle class that inherits from the Base class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter fucntion width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter fucntion for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter fucntion for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function for x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter fucntion for x"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes and returns area of a rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Prints the rectangle instance with #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """Return a string representation of Rectangle"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Updates the parameters of Object with values from args"""
        attr = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i, v in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], v)
                else:
                    break
        else:
            for k, v in kwargs.items():
                if k in attr:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle class"""
        _dict = {'id': self.id, 'width': self.__width, 'height': self.__height,
                 'x': self.__x, 'y': self.__y}
        return _dict
