#!/usr/bin/python3
""" A class for a Square """


class Square:

    def __init__(self, size=0, position=(0, 0)):
        """ Args: param1 (size): Size of the square """
        self.size = size

    @property
    def position(self):
        """ Retrieves position """
        self.__position = position
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets position of Square """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """ Retrieves size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets property of size """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """ Area of square """
        area = self.__size * self.__size

        return area

    def my_print(self):
        """ Prints in stdout the square with chars # """
        if (self.__size == 0):
            print()
        else:

            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
