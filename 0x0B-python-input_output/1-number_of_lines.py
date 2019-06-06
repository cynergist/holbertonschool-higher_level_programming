#!/usr/bin/python3
import os

""" a function that returns number of lines in a text file
"""


def number_of_lines(filename=""):
    numlines = 0
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            numlines = numlines + 1
    return numlines

    """ Arg1: string containing filename
    Arg2: mode can be 'r' when file will only be read,
    'w' for writing, and 'a' opens file for appending, 'r+
    for both reading and writing, overwrite mode, unicode
    where nos represent characters
    Arg3: UTF-8 encoding
    """
