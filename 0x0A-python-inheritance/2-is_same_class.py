#!/usr/bin/python3
""" Function that checks if obj is exactly instance of a_class """


def is_same_class(obj, a_class):
    """ Args: param1 (obj): instance
    param2 (a_class): type of object to check
    """
    if type(obj) is a_class:
        return True
    else:
        return False
