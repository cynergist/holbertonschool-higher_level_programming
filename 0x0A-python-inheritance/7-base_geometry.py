#!/usr/bin/python3
''' BaseGeometry module. '''


class BaseGeometry():
    ''' A BaseGeometry parent class. '''
    def __init__(self):
        ''' Creates an instance of BaseGeometry. '''
        pass

    def area(self):
        ''' Method to calculate area '''
        raise TypeError('area() is not implemented')

    def integer_validator(self, name, value):
        ''' Validates value.

        Exceptions:
        1. Raise TypeError if value is not an int
        2. Raise ValueError if value is less than or equal to 0
        '''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
