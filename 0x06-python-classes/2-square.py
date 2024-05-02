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
