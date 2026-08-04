#!/usr/bin/python3
"""Module that defines a function to print a square of '#' characters."""


def print_square(size):
    """Print a square with the character '#'.

    Args:
        size: the size length of the square, must be an integer >= 0.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is an integer less than 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
