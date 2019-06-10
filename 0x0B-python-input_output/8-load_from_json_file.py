#!/usr/bin/python3
import json

'''
a function that creates an Object from a JSON file
'''


def load_from_json_file(filename):
    '''
    Arg1: filename is the "JSON file"
    '''
    with open(filename, encoding=None) as myfile:
        return json.load(myfile)
