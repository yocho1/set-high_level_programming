#!/usr/bin/python3
"""Module to convert class to JSON-serializable dict."""


def class_to_json(obj):
    """Return dictionary description for JSON serialization of an object."""
    return obj.__dict__
