#!/usr/bin/python3

""" Defines a class square"""


class Square():
    """ Defines a square"""

    def __init__(self, size=0):
        """Initializes self"""
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value"""
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def __eq__(self, other):
        """equal to"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """not equal to"""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """less than"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """less than or equal to"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """greater than"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """greater than or equal to"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented