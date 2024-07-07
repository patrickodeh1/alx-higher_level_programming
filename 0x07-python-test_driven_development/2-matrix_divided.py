#!/usr/bin/python3
"""
Divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    """
    if not isinstance(matrix, list) or\
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list \
        of lists) of integers/floats")

    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of \
        lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float('inf'):
        return [[0.0 for _ in row] for row in matrix]

    return [[round(elem / div, 2) for elem in row] for row in matrix]
