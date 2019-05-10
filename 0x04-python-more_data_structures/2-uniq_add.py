#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    a function that adds unique integers in a list only once
    """
    return sum(set(my_list))
    """
    first return the unique set of my_list and then sum all of it
    """
