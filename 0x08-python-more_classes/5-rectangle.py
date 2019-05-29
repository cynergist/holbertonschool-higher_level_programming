#!/usr/bin/python3
""" A module containig a rectangle class """


class Rectangle:
    """ A class for a rectangle. Attributes: width and height """

    def __init__(self, width=0, height=0):
        """ Args: param1 (width): Width of the rectangle
        param2 (height): Height of the rectangle
        """
        self.__width = width

        self.__height = height

    def __del__(self):
        print ("Bye rectangle...")

    @property
    def width(self):
        """ Retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets property of width """
        """ TypeError exception for width must be an integer """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets property of height """
        """ TypeError exception for height must be an integer """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Returns the rectangle area only """
        area = self.__width * self.__height

        return area

    def perimeter(self):
        """ Returns the rectangle perimeter only """
        if not self.__width or not self.__height:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)

        return perimeter

    def __str__(self):
        """ Returns informal printable str of the rectangle instance """
        if not self.__width or not self.__height:
            return ""
        else:
            return (self.__height * ("#" * self.__width + "\n"))[:-1]

    def __repr__(self):
        """ Returns official printable str of the rectangle instance """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
