#!/usr/bin/python3
''' Module for Rectangle inherited from Base '''

from models.base import Base


class Rectangle(Base):
    ''' A child class for a Rectangle.
        Arg1: width of the rectangle
        Arg2: height of the rectangle
        Arg3: x - horizontal offset of the rectangle
        Arg4: y - vertical offset of the rectangle
        Arg 5: id
        '''
    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Creates an intstance of Rectangle '''
        ''' access parent class Base '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' Attribute retrieves width of Rectangle '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Sets property of width
        TypeError and ValueError exceptions for width
        must be an integer greater than 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' Attribute retrieves height of Rectangle '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Sets property of height
        TypeError and ValueError exceptions for height
        must be an integer greater than 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' Returns the horizontal offset of the Rectangle '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' Sets property of x
        TypeError and ValueError exceptions for x
        must be an integer greater than 0
        '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' Returns the verticle offset of the Rectangle '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' Sets property of y
        TypeError and ValueError exceptions for y
        must be an integer greater than 0
        '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' Method returns area of the Rectangle '''
        return self.__width * self.__height

    def display(self):
        ''' Method prints hashes to stdout of the Rectangle instance '''
        print(('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') *
               self.__height)[:-1])

    def __str__(self):
        ''' Returns string representation of the Rectangle '''
        return '[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}'.format(self.id,
                                                               self.__x,
                                                               self.__y,
                                                               self.__width,
                                                               self.__height)

    def to_dictionary(self):
        ''' Returns dictionary representation of the Rectangle '''
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
         'x': self.__x, 'y': self.__y}
