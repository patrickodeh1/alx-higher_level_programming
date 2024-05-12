#!/usr/bin/python3

""" Defines a class square based on 6-square.py"""


class Square():
    """ Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes self"""
        self.size = size
        self.position = position

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

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

    @property
    def position(self):
        """retrieves the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value for position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not isinstance(value[0], int) or not isinstance
                (value[1], int) or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """prints a square"""
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
        else:
            print()

    def __str__(self):
        """string representation of a square"""
        res = ""
        if self.__size != 0:
            for _ in range(self.__position[1]):
                res += "\n"
            for _ in range(self.__size):
                res += " " * self.position[0] + "#" * self.__size + "\n"
        else:
            res += "\n"
        return res[:1]
