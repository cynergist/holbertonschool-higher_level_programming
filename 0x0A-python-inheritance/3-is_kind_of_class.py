#!/usr/bin/python3
""" Function that checks if obj isinstance of a_class """


def is_kind_of_class(obj, a_class):
    """ Args: param1 (obj): instance
    param2 (a_class): type of object to check
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
