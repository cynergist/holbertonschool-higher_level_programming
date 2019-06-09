#!/usr/bin/python3
''' Rectangle module. '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' A child class for a square. '''
    def __init__(self, size):
        ''' Creates an instance of a Square.

        Arg1: equal width and height of the square.
        '''
        self.__size = self.integer_validator('size', size)

    def area(self):
        ''' Method returns area of square, or size squared. '''
        return self.__size ** 2

    def __str__(self):
        ''' String representation of a square '''
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
