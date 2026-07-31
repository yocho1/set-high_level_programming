#!/usr/bin/python3
"""Module that defines a function to write to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file and return the number of chars."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
