#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    function returns a new dictionary with all values multiplied by 2.
    all values are integers.
    returns a new dictionary.
    no modules imported.
    using dictionary comprehension
    """
    return {x: y*2 for x, y in list(a_dictionary.items())}
