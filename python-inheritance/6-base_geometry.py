#!/usr/bin/python3
"""Module that defines a BaseGeometry class with an area method."""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area method."""

    def area(self):
        """Raise an exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")
