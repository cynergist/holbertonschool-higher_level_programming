#!/usr/bin/python3

'''
a function that appends a string to the end of a text \
file (UTF8) and returns num of chars added
'''


def append_write(filename="", text=""):
    '''
    Arg1: filename myfile
    Arg2: text is number of chars written
    '''
    with open(filename, mode='a', encoding='utf-8') as myfile:
        return myfile.write(text)
