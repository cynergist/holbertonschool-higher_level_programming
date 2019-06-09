#!/usr/bin/python3
import json

'''
a function that returns the JSON representation of an object
'''


def to_json_string(my_obj):
    '''
    Arg1: a string object
    '''
    return json.JSONEncoder().encode(my_obj)
