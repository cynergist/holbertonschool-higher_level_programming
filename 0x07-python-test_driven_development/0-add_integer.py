#!/usr/bin/python3
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

def add_integer(a, b=98):
    """function adds two integers

    Args:
        param1: An integer or a float.
        param2: An integar or a float.

    Returns:
        The addition of two integers
    """
    
    if type(a) is not int or float:
        raise TypeError("a must be an integer")

    if type(b) is not int or float:
        raise TypeError("b must be an integer")

### a and b must be first casted to integers if they are float
        return a + b