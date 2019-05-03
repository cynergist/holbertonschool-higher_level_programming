#!/usr/bin/python3
if __name__ == "__main__":
    """
    Note: it is possible to use sys, but we are only concerned
    withe argv, so will only import this module
    """
    from sys import argv

    if len(argv) is 2:
        print("1 argument:\n1: {}".format(str(argv[1]))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
              print("{:d}: {:s}\n".format(i + 1, argv[i + 1]))
    else:
        print("0 arguments.")
