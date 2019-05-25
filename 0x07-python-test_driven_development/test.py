#!/usr/bin/python3
def testable(x):
    r"""
    The `testable` function returns the square root of its parameter, or 3, whichever is larger.
"""
    if x < 9:
        return 3.0
    return x ** 0.5
