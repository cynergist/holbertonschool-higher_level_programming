#!/usr/bin/python3
def max_integer(my_list=[]):

    if my_list:
        # If my_list is not empty
        my_list = sorted(my_list, reverse=True)
        # Sort my_list and reverse it, reassign to my_list
        return my_list[0]
    else:
        return None
