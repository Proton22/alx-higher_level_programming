#!/usr/bin/python3
"""
   4-inherits_from: a class
"""


def inherits_from(obj, a_class):
    """
        returns if the object is an instance.
        Args:
            obj: object.
            a_class: class.
        Returns:
               True: if the object is an instance of a class
               otherwise false.
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
