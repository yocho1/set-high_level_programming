#!/usr/bin/python3
"""Defines a function that multiplies two matrices using numpy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using numpy.

    Lets numpy raise its own native exceptions (TypeError/ValueError)
    when the inputs cannot be converted or multiplied, instead of
    manually validating m_a and m_b.

    Args:
        m_a: the first matrix
        m_b: the second matrix

    Returns:
        numpy.ndarray: the result of multiplying m_a by m_b
    """
    return np.matmul(m_a, m_b)
