#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    else:
        a_dictionary[value] = key=""
        return a_dictionary
