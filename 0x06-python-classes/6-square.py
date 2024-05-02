#!/usr/bin/python3

""" Defines a class square"""


class Square():
    """ Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes self"""
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints a square"""
        if self.__size != 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()

    @property
    def position(self):
        """retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value for position"""
        if len(self.__position) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
