"""
program: NumberGuesser_test.py
author: kyle godwin
last date modified: 18 april 2023

test program for NumberGuesser_class.py
"""
import unittest
from NumberGuesser_class import *
from NumberGuesser_class import NumberGuesser as n


class NumberGuesserTest(unittest.TestCase):

    def setUp(self):  # set up class
        self.num = n(5)

    def tearDown(self):  # tear down class
        del self.num

    def test_object_created_required_attributes(self):  # test required attributes for class
        self.assertEqual(self.num.random_number, 5)

    def test_get_number_function(self):
        self.assertEqual(self.num.get_number_list(), [])

    def test_get_number_function_2(self):
        self.num.guessed_list = [1, 2, 3, 4, 5]
        self.assertEqual(self.num.get_number_list(), [1, 2, 3, 4, 5])

    def test_guess_number_function(self):
        self.num.guessed_list = [2, 3, 4, 5]
        self.assertEqual(self.num.guess_number(1), self.num.guessed_list)

    def test_str(self):
        self.assertEqual(str(self.num), "5")

    def test_repr(self):
        self.assertEqual(repr(self.num), "NumberGuesser(5)")

    def test_object_not_created_error_random_number(self):  # test random number
        with self.assertRaises(OutofRangeException):
            num_guess = n(99)

    def test_object_not_created_error_guess_number(self):  # test guess number
        with self.assertRaises(OutofRangeException):
            num_guess = n(11)


if __name__ == '__main__':
    unittest.main()
