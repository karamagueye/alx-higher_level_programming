#!/usr/bin/python3
"""Defines a class-checking function."""
def is_same_class(obj, a_class):
    """check if an object is exactly an instance of a given class.
    Return:if obj is exactly an instance of class - True.
    otherwise - False.
    """
    if type(obj) == a_class:
        return True
        return False
