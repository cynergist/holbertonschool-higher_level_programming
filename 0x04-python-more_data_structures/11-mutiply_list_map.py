#!/usr/bin/python3
def mutiply_list_map(my_list=[], number=0):
    """ Use lambda in convention "lambda key: key operator number, listname"
    """
    return list(map(lambda x: x * number, my_list))
