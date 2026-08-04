#!/usr/bin/python3
"""Module that defines a function to multiply two matrices with NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a: the first matrix, a list of lists of integers or floats.
        m_b: the second matrix, a list of lists of integers or floats.

    Returns:
        numpy.ndarray: the product of m_a and m_b.

    Raises:
        ValueError: if m_a and m_b can't be multiplied.
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
