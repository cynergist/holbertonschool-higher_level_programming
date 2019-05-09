#!/usr/bin/python3
if __name__ == "__main__":
    """
    Note: it is possible to use sys, but we are only concerned
    with the argv, so will only import this module
    """
    from sys import argv

    len = len(argv)

    if len is 1:
        print("0 arguments.")
    elif len is 2:
        print("1 argument:\n1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(len - 1))
        for args in range(1, len):
            print("{:d}: {:s}".format(args, argv[args]))
