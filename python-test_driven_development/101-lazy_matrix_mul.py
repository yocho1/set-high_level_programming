#!/usr/bin/python3
"""Defines a function that multiplies two matrices using numpy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using numpy.

    Args:
        m_a (list of lists of ints/floats): the first matrix
        m_b (list of lists of ints/floats): the second matrix

    Returns:
        numpy.ndarray: the result of multiplying m_a by m_b

    Raises:
        TypeError: if m_a or m_b is not a list of lists of ints/floats,
            or if their rows are not all of the same size
        ValueError: if m_a or m_b is empty, or if m_a and m_b
            cannot be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if not row:
            raise ValueError("m_a can't be empty")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if not row:
            raise ValueError("m_b can't be empty")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    size_a = len(m_a[0])
    for row in m_a:
        if len(row) != size_a:
            raise TypeError(
                "each row of m_a must should be of the same size")

    size_b = len(m_b[0])
    for row in m_b:
        if len(row) != size_b:
            raise TypeError(
                "each row of m_b must should be of the same size")

    if size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)
