#!/usr/bin/python3
""" A class for BaseGeometry

"""


class BaseGeometry():

    """ A class. """
    def __init__(self):
        """ Creates an instance of BaseGeometry. """
        pass

    def area(self):
        """ Raises a TypeError. """
        raise TypeError('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validates an argument

        Exceptions:
        1. Raise TypeError if value is not an int
        2. Raise ValueError if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
