#!/usr/bin/python3
"""This module defines a Square class with getter and setter."""


class Square:
    """A class that defines a square with size getter and setter."""

    def __init__(self, size=0):
        """Initialize a new Square instance."""
        self.size = size  # Uses the setter for validation

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
