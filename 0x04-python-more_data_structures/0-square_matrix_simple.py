#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    we can solve this as a list comprehension inside another list comprehension
    """
    return [[x ** 2 for x in row] for row in matrix]
