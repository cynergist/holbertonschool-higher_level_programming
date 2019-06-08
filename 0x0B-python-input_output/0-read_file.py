#!/usr/bin/python3


""" a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):

    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")

        """ Arg1: string containing filename
        Arg2: mode can be 'r' when file will only be read,
        'w' for writing, and 'a' opens file for appending, 'r+
         for both reading and writing
         , overwrite mode, unicode where nos represent
         characters
         Arg3: UTF-8 encoding
         """
