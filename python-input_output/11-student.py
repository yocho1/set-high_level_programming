#!/usr/bin/python3
"""Module that defines a Student class with serialization/deserialization."""


class Student:
    """Student class with serialization and reload capabilities."""

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

    def reload_from_json(self, json):
        """Replace all attributes from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
