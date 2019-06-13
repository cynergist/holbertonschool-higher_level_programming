#!/usr/bin/python3
''' Unittest for rectangle.py '''

from models.base import Base
from models.rectangle import Rectangle

import unittest


class TestRectangle(unittest.TestCase):
    ''' Unittest for rectangle '''

    @classmethod
    def setUpClass(cls):
        ''' Setting up testing environment for Rectangle '''
        Rectangle = Rectangle.__nb_objects = 0
        Base = Base.__nb_objects = 0
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(2, 2)
        cls.r3 = Rectangle(3, 4, 1)
        cls.r4 = Rectangle(4, 6, 3, 2)
        cls.r5 = Rectangle(5, 4, 3, 2, 101)

    def test_ints_width(self):
        ''' Test for adding ints to width '''
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 3)
        self.assertEqual(self.r4.width, 4)
        self.assertEqual(self.r5.width, 5)

    def test_ints_depth(self):
        ''' Test for adding ints to depth '''
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 4)
        self.assertEqual(self.r4.width, 6)
        self.assertEqual(self.r5.width, 4)

    def test_id_incrementation(self):
        ''' Test for incrementation of id '''
        self.assertEqual(eself.r1.id, 2)
        self.assertEqual(self.r2.id, 3)
        self.assertEquals(self.r3.id, 4)
        self.assertEqual(self.r4.id, 5)
        self.assertEqual(self.r5.id, 101)

    def test_class_type(self):
        ''' Unittest for correct class type '''
        self.assertEqual(type(self.r1), Rectangle)

    def test_instantiation(self):
        ''' Unittest for instantiation of class '''
        self.assertTrue(self.r1)

if __name__ == '__main__':
    unittest.main()
