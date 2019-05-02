#!/usr/bin/python3
"""
Note: the filename passed into from <filename> import <function names>
contains functions for addition, subraction,
multiplication, and division.
"""
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
"""
If the module is imported, the code is not run, so "import add, sub, mul,
or div" will not run code. This is often used either to provide a convenient
user interface to a module, or for testing purposes like running the module
as a script executes a test suite.
https://docs.python.org/3.4/tutorial/modules.html
"""
