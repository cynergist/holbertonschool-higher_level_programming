#!/usr/bin/python3
''' Module for Base '''

from models.base import Base


class Rectangle(Base):
    ''' A child class for a rectangle. '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Creates an intstance of Rectangle
        Arg1: width of the rectangle
        Arg2: height of the rectangle
        Arg3: x
        Arg4: y
        '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        ''' access parent class Base '''
        super().__init__(id)

    @property
    def width(self):
        ''' Attribute retrieves width of Rectangle '''
        return self.__width

    @width.setter
    def width(self, w):
        ''' Sets property of width
        TypeError and ValueError exceptions for width
        must be an integer greater than 0
        '''
        if type(w) is not int:
            raise TypeError("width must be an integer")
        if w < 0:
            raise ValueError("width must be > 0")

        self.__width = w

    @property
    def height(self):
        ''' Attribute retrievew height of Rectangle '''
        return self.__height

    @height.setter
    def height(self, h):
        ''' Sets property of height
        TypeError and ValueError exceptions for height
        must be an integer greater than 0
        '''
        if type(h) is not int:
            raise TypeError("height must be an integer")
        if h < 0:
            raise ValueError("width must be > 0")
        self.__height = h

    @property
    def x(self):
        ''' Creates an attribute of Rectangle '''
        return self.__x

    @x.setter
    def x(self, new_x):
        ''' Sets property of x
        TypeError and ValueError exceptions for x
        must be an integer greater than 0
        '''
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        ''' Creates an attribute of Rectangle '''
        return self.__y

    @y.setter
    def y(self, new_y):
        ''' Sets property of y
        TypeError and ValueError exceptions for y
        must be an integer greater than 0
        '''
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y
