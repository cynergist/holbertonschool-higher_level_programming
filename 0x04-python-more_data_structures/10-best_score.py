#!/usr/bin/python3
def best_score(a_dictionary):
    """
    function returns a key with the biggest integer value.
    all values are only integers.
    if no score found, return None
    all students have a different score
    no module imported
    """
    # Validation statement for no score found
    if not a_dictionary:
        return None
    else:
        # .keys converts dict to a list, then sorted, take last key element
        return sorted(a_dictionary.keys())[-1]
