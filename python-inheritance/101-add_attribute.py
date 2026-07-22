#!/usr/bin/python3
"""Module that defines a function to add attributes to objects."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
