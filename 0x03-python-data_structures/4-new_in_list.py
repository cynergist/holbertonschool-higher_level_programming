#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_my_list = my_list[:]
    if idx < 0 or idx > len(copy_my_list) - 1:
        return copy_my_list
    else:
        copy_my_list[idx] = element
        return copy_my_list