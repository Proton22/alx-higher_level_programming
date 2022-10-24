#!/bin/python3
"""
    2-is_same_class: specified class
"""


def is_same_class(obj, a_class):
    """
       Returns True if the object is exactly an instance.
       Args:
           obj: object.
           a_class: an instance of the specified class.
       Returns:
              True if the object is exactly the specified class
              otherwise False
    """
    return isinstance(obj, a_class)
