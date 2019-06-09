#!/usr/bin/python3
import json

'''
a function that returns a Python data struct \
object represented by a JSON string
'''


def from_json_string(my_str):
    '''
    Arg1: a string object
    '''
    return json.JSONDecoder().decode(my_str)
