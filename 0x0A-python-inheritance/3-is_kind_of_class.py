#!/usr/bin/python3
""" Function that checks if obj isinstance of a_class """

def is_kind_of_class(obj, a_class):
    """ Args: param1 (obj):
    param2 (a_class):
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
