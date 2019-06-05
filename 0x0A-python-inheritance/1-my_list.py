#!/usr/bin/python3
""" MyList class inherited from list """


class MyList(list):

    def print_sorted(self):
        """ Args: self
        """
        print(sorted(self))
