#!/usr/bin/python3
"""This module defines a Square class with comparison operators."""


class Square:
    """A class that defines a square with comparison capabilities."""

    def __init__(self, size=0):
        """Initialize a new Square instance."""
        self.size = size

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Equality comparator based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparator based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparator based on area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
