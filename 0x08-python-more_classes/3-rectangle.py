#!/usr/bin/python3
"""a class rectangle"""


class Rectangle():
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value for the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value for the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """computes the area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """computes the perimeter of a rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def print_rectangle(self):
        """prints rectangle using #"""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.height):
                for j in range(self.width):
                    rect += "#"
                if i != self.height - 1:
                    rect += "\n"
            return rect

    def __str__(self):
        """string representation of the rectangle"""
        return self.print_rectangle()

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "<{} object>".format(type(self).__name__)
