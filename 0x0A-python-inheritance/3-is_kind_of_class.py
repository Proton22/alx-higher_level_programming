#!/usr/bin/python3
"""
    3-is_kind_of_class: object is an instance of a class
"""

def is_kind_of_class(obj, a_class):
    """
       function that returns a class that inherited from it.
       Args:
            obj: object class.
            a_class: class
       Returns:
               True:  if the object is an instance of a class
               otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
