#!/usr/bin/python3
"""Module that defines a function to append text after a search string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing search_string."""
    new_lines = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(new_lines)
