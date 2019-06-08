#!/usr/bin/python3


"""
a function that reads n lines of a UTF8 text file and prints to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    Arg1: filename: myfile
    Arg2: nb_lines: number of lines in the file
    """
    with open(filename, mode="r", encoding="utf-8") as myfile:
        if nb_lines <= 0:
            print(myfile.read(), end="")
        else:
            for count in range(nb_lines):
                print(myfile.readline(), end="")
