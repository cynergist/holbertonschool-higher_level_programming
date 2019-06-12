#!/usr/bin/python3
''' Module for Base '''


class Base():
    ''' A parent class '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Creates an instance of Base.
        Arg1: variable id is initialized at None
        '''
        if id is not None:
            self.id = id
            ''' id here is an attribute of the class '''
        else:
            type(self).__nb_objects += 1
            ''' _Base.__nb_objects '''
            self.id = type(self).__nb_objects
