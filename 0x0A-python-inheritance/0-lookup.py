#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of available attributes of an obeject."""
    return (dir(obj))
