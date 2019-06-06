#!/usr/bin/python3
""" Function that returns True iff obj isinstance of a class """


def inherits_from(obj, a_class):
    """ Args: param1 (obj): instance
    param2 (a_class): type of object to check
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    else:
        return False
