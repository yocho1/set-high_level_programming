#!/usr/bin/python3
"""Module that defines a MyInt class with inverted == and != operators."""


class MyInt(int):
    """MyInt class with inverted == and != operators."""

    def __eq__(self, other):
        """Invert the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the != operator."""
        return super().__eq__(other)
