#!/usr/bin/python3
"""

This module is composed by a function that print a name

"""
def say_my_name(first_name, last_name=""):
    """ Function that print out a name.

    Args:
        first_name: the first name to be printed.
        last_name: the second name to be printed.
    Raise:
         TypeError: if the element is not a string.
    Returns:
           printing the first and last name.
    """
    if not isinstance (first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance (last_name, str):
        raise TypeError("last_name must be a string")
    return ("My name is {} {}".format(first_name, last_name))
