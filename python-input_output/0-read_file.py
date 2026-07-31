#!/usr/bin/python3
"""Module that defines a function to read and print a file."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
