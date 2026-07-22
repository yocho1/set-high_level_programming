#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """MyList class that inherits from list with a print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
