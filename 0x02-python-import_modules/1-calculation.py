#!/usr/bin/python3
"""
Note: the file calculator_1 contains functions for addition, subraction,
multiplication, and division. [from <filename> import <function name(s)]
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
user interfaceto a module, or for testing purposes like running the module
as a scriptexecutes a test suite.
https://docs.python.org/3.4/tutorial/modules.html
"""
