#!/usr/bin/python3
"""Module that defines a function to print text with indentation."""


def text_indentation(text):
    """Print a text, adding 2 new lines after each '.', '?' or ':'.

    Args:
        text: the text to print, must be a string.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip(), end="")
