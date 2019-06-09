#!/usr/bin/python3

''' a function that writes a text file (UTF8); returns num of chars written '''


def write_file(filename="", text=""):
    '''
    Arg1: filename myfile
    Arg2: text is number of chars written
    '''
    numchars = 0
    with open(filename, mode='w', encoding='utf-8') as myfile:
        return myfile.write(text)
