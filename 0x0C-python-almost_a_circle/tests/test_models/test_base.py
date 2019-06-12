#!/usr/bin/python3
''' Unittest for base.py '''

from models.base import Base

import unittest


class TestBase(unittest.TestCase):
    ''' Unittest for base '''
    def test_class_type(self):
        ''' Unittest for correct class type '''
        b = Base()
        self.assertTrue(type(b), Base)

    def test_instantiation(self):
        ''' Unittest for instantiation of class '''
        b = Base()
        self.assertTrue(b, Base)
    '''
    def test_no_arg(self):
        Unittest for base incrementation beginning with 1 for id
        b = Base()
        self.assertEqual(b.id, 1)
    '''
    def test_no_list(self):
        ''' Unittest for empty list '''
        b = Base([])
        self.assertEqual(b.id, [])

    def test_no_tuple(self):
        ''' Unittest for empty tuple '''
        b = Base(())
        self.assertEqual(b.id, ())

    def test_no_dict(self):
        ''' Unittest for empty dictionary '''
        b = Base({})
        self.assertEqual(b.id, {})

    def test_one_arg(self):
        ''' Unittest for base using 10 for id'''
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_negative_value(self):
        ''' Unittest for base using -1 for id '''
        b = Base(-1)
        self.assertEqual(b.id, -1)

    def test_zero_value(self):
        ''' Unittest for base using 0 for id '''
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_string(self):
        ''' Unittest for base using "hello" for id '''
        b = Base('hello')
        self.assertEqual(b.id, 'hello')

    def test_dict(self):
        ''' Unittest for base using a dict for id '''
        b = Base({'name': 'cyn', 'address': 'berkeley'})
        self.assertEqual(b.id, {'name': 'cyn', 'address': 'berkeley'})

if __name__ == '__main__':
    unittest.main()
