#!/usr/bin/python3
"""define a function to matrix division."""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""
    if (not isinstance(matrix, list)
            or matrix == [] or
            any(not isinstance(row, list)
                or (not isinstance(num, (int, float)))
                for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
