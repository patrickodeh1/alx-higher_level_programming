#!/usr/bin/python3
"""class magicclass"""

import math


class MagicClass:
    """defines magic class"""
    def __init__(self, radius=0):
        """initialize"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """defines the area"""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """a circumference"""
        return 2 * math.pi * self.__radius
