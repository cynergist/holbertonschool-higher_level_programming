#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        result = a / b
        """ result is value of division """
    except:
        """ otherwise result is None """
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
