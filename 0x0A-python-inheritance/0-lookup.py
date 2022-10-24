#!/usr/bin/python3
"""
   0-lookup module
"""


def lookup(obj):
    """
        Returns the list of available attributes and methods.
        Args:
             obj: list of attribute.
        Results:
                lists of bojects.
    """
    return(dir(obj))
