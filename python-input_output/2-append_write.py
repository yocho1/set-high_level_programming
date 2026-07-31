#!/usr/bin/python3
"""Module that defines a function to append to a file."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 text file and return the number of chars."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
