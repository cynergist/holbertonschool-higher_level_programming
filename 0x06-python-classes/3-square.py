#!/usr/bin/python3
""" A class for a Square """


class Square:

    def __init__(self, size=0):
        """Args: param1 (__size): Size of the square, a private attribute
        """
        if type(size) != int:
                raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Area of square """
        area = self.__size * self.__size

        return area
