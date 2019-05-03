#!/usr/bin/python3
import sys

if len(sys.argv) is 1:
    print("0 arguments.")
if len(sys.argv) is 2:
    print("1 argument:\n1: {}".format(str(sys.argv[1]))
if len(sys.argv) > 2:
    print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv) - 1):
          print("{:d}: {:s}\n".format(i + 1, sys.argv[i + 1]))