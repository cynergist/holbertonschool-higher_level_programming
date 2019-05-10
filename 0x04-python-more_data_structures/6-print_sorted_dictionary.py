#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # store your key in a variable and your value in a variable
    for key, value in sorted(a_dictionary.items()):
        # sorted(key)
        print("{}: {}".format(key, value))
        # sorted(a_dictionary.key=str.lower)
