#!/usr/bin/python3
"""Module that defines a LockedClass with restricted attributes."""


class LockedClass:
    """A class that prevents dynamic attribute creation except first_name."""
    __slots__ = ["first_name"]
