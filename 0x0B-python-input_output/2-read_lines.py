#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):

    with open(filename, mode="r", encoding="utf-8") as myfile:
#        count = 1
#        if len(myfile.readlines()) < nb_lines <= 0:
        if len(myfile.readlines()) < nb_lines:
            print(myfile.read(), end="")
        else:
            for count in range(nb_lines):
                print(myfile.readline(), end="")
                print(count)
                print(len(myfile.readlines()))
