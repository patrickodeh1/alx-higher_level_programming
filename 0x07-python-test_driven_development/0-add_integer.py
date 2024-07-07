#!/usr/bin/python3
"""sums up two integers"""


def add_integer(a, b=98):
    """Adds two integers"""

    if isinstance(a, float):
        if a == float('inf') or a == float('-inf') or a != a:  # checks for inf and NaN
            raise TypeError("a must be an integer")
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")

    if isinstance(b, float):
        if b == float('inf') or b == float('-inf') or b != b:  # checks for inf and NaN
            raise TypeError("b must be an integer")
        b = int(b)
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
