#!/usr/bin/python3
"""This module defines a Square class with string representation."""


class Square:
    """A class that defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using '#' with position offset."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return string representation of the square."""
        if self.__size == 0:
            return ""

        result = []
        for _ in range(self.__position[1]):
            result.append("")

        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(result)
