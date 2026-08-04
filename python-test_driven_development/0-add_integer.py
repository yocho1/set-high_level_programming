#!/usr/bin/python3
"""Module that defines a function to add two integers."""


def add_integer(a, b=98):
    """Add two integers together.

    Args:
        a: the first value, must be an int or a float.
        b: the second value, must be an int or a float. Defaults to 98.

    Returns:
        int: the sum of a and b, after casting both to int.

    Raises:
        TypeError: if a is not an int or a float.
        TypeError: if b is not an int or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
