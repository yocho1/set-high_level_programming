#!/usr/bin/python3
"""Module that defines a function to multiply two matrices."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: the first matrix, a list of lists of integers or floats.
        m_b: the second matrix, a list of lists of integers or floats.

    Returns:
        list: a new matrix, the product of m_a and m_b.

    Raises:
        TypeError: if m_a or m_b is not a list.
        TypeError: if m_a or m_b is not a list of lists.
        ValueError: if m_a or m_b is empty.
        TypeError: if m_a or m_b contains a non integer/float element.
        TypeError: if a row of m_a or m_b is not the same size as
            the other rows.
        ValueError: if m_a and m_b can't be multiplied.
    """
    def validate(matrix, name):
        if not isinstance(matrix, list):
            raise TypeError("{} must be a list".format(name))
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError("{} must be a list of lists".format(name))
        if matrix == [] or matrix == [[]]:
            raise ValueError("{} can't be empty".format(name))
        for row in matrix:
            for elem in row:
                if not isinstance(elem, (int, float)) or \
                        isinstance(elem, bool):
                    raise TypeError(
                        "{} should contain only integers or floats".format(
                            name))
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise TypeError(
                    "each row of {} must be of the same size".format(name))

    validate(m_a, "m_a")
    validate(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result
