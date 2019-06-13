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
        ''' Creates an attribute of Rectangle '''
        return self.__width

    @width.setter
    def width(self, w):
        self.__width = w

    @property
    def height(self):
        ''' Creates an attribute of Rectangle '''
        return self.__height

    @height.setter
    def height(self, h):
        self.__height = h

    @property
    def x(self):
        ''' Creates an attribute of Rectangle '''
        return self.__x

    @x.setter
    def x(self, new_x):
        self.__x = new_x

    @property
    def y(self):
        ''' Creates an attribute of Rectangle '''
        return self.__y

    @y.setter
    def y(self, new_y):
        self.__y = new_y
