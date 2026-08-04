#!/usr/bin/python3
"""Module that defines a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a given divisor.

    Args:
        matrix: a list of lists of integers or floats. Every row must
            have the same length.
        div: an integer or a float, the divisor. Cannot be 0.

    Returns:
        list: a new matrix with every element divided by div and
            rounded to 2 decimal places.

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats.
        TypeError: if the rows of matrix don't all have the same size.
        TypeError: if div is not a number.
        ZeroDivisionError: if div is equal to 0.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_matrix)
        for elem in row:
            if not isinstance(elem, (int, float)) or isinstance(elem, bool):
                raise TypeError(err_matrix)

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix
