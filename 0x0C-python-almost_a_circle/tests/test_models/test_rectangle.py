#!/usr/bin/python3
''' Unittest for rectangle.py '''

from models.base import Base
from models.rectangle import Rectangle

import unittest


class TestRectangle(unittest.TestCase):
    ''' Unittest for rectangle '''

    def test_class_type(self):
        ''' Unittest for correct class type '''
        r1 = Rectangle(5, 10)
        self.assertTrue(type(r1), Rectangle)

if __name__ == '__main__':
    unittest.main()
