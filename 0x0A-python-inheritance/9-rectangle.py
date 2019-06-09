#!/usr/bin/python3
''' Rectangle module. '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' A child class for a rectangle. '''
    def __init__(self, width, height):
        ''' Creates an instance of Rectangle.

        Arg1: width of the rectangle.
        Arg2: height of the rectangle.
        '''
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

    def area(self):
        ''' Method returns area of rectangle. '''
        return self.__width * self.__height

    def __str__(self):
        ''' String representation of a rectangle. '''
        return '[Rectangle] ' \
            + str(self.__width) + '/' + str(self.__height)
