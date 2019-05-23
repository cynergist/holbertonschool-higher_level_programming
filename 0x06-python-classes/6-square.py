#!/usr/bin/python3
""" A class for a Square """


class Square:

    def __init__(self, size=0, position=(0, 0)):
        """ Args: param1 (size): Size of the square
            param2 (position): Position (over and down) of square
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """ Only retrieves position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets position of Square """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        """ Executes below only when we pass Error checks """
        self.__position = value

    @property
    def size(self):
        """ Only retrieves size """
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
            if (self.__position[1] > 0):
                for n in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                if (self.__position[0] > 0):
                    for s in range(self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
