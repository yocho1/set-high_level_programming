#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON."""


class Student:
    """Student class with first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation with optional filtering."""
        if attrs is None:
            return self.__dict__

        if (isinstance(attrs, list) and
                all(isinstance(item, str) for item in attrs)):
            return {key: val for key, val in self.__dict__.items()
                    if key in attrs}

        return self.__dict__
