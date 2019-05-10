#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    a_dictionary[key] = value
    return a_dictionary
    """
    a_dictionary.pop(key, None)
    return a_dictionary
