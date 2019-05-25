#!/usr/bin/python3
"""
    matrix divides by div
"""
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

def matrix_divided(matrix, div):
    """function divides all elements of a matrix

    Args:
        param1: A matrix, or a list of lists of integers, floats, or other types
        param2: An integer or a float.

    Returns:
        A new matrix
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisonError("division by zero")
    for row in matrix:      
        for i in row: 
            if type(i) is not int and type(i) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    return [[x / div for x in row] for row in matrix]
