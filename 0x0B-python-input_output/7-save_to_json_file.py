#!/usr/bin/python3
import json

'''
a function that writes an Object to a text file, using a JSON representation
'''


def save_to_json_file(my_obj, filename):
    '''
    Arg1: an object
    Arg2: filename is a text tile
    '''
    with open(filename, mode='w', encoding=None) as myfile:
        return json.dump(my_obj, myfile)
