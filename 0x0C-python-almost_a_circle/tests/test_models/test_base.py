xc#!/usr/bin/python3
''' Unittest for base.py '''

from models.base import Base

import unittest


class TestBase(unittest.TestCase):
    ''' Unittest for base '''

    @classmethod
    def setUpClass(cls):
        ''' Setting up testing environment for Base '''

        Base._Base__nb_objects = 0
        cls.b1 = Base()
        cls.b10 = Base()
        cls.b2 = Base(0)
        cls.b3 = Base(50)
        cls.b4 = Base(-5)
        cls.b5 = Base(256)

    def test_class_type(self):
        ''' Unittest for correct class type '''
        self.assertEqual(type(self.b1), Base)

    def test_instantiation(self):
        ''' Unittest for instantiation of class '''
        self.assertTrue(self.b1)

    def test_incrementation(self):
        ''' Unittest for incrementation of __nb_objects '''
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b10.id, 2)

    def test_ints(self):
        ''' Unittest id passing 0,pos,neg,outside nsmallposints '''
        self.assertEqual(self.b2.id, 0)
        self.assertEqual(self.b3.id, 50)
        self.assertEqual(self.b4.id, -5)
        self.assertEqual(self.b5.id, 256)

if __name__ == '__main__':
    unittest.main()
