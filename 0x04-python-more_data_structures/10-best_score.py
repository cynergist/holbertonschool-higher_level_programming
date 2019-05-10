#!/usr/bin/python3
def best_score(a_dictionary):
    """
    function returns a key with the biggest integer value.
    all values are only integers.
    if no score found, return None
    all students have a different score
    no module imported
    """
    name = max(a_dictionary, key = lambda name: a_dictionary[name])
    points = a_dictionary[name]
    return name

    # key, value = max(a_dictionary.iteritems(), key = lambda p: p[1])
    # maximum = max(a_dictionary, key=a_dictionary.get)
    # return a_dictionary[maximum]
    # max(a_dictionary.items(), key=lambda k: k[1])
