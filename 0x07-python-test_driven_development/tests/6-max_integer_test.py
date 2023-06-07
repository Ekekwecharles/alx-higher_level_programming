#!/usr/bin/python3
"""Unittest for the module 6-max_integer.py
    def max_integer(list=[]):
    Function to find and return the max integer in a list ofIf the list
    is empty, the function returns None"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_module_docstring(self):
        """Test module docstring"""
        mod = __import__('6-max_integer').__doc__
        self.assertTrue(len(mod) > 1)

    def test_function_docstring(self):
        """Test function docstring"""
        func = max_integer.__doc__
        self.assertTrue(len(func) > 1)

    def test_max_at_beginning(self):
        """Test list with max value at the begginning"""
        max_at_beginning = [10, 9, 8, 7, 6]
        self.assertEqual(max_integer(max_at_beginning), 10)

    def test_max_at_end(self):
        """Test list with max value at the end"""
        max_at_end = [10, 9, 8, 7, 6, 12]
        self.assertEqual(max_integer(max_at_end), 12)

    def test_max_in_mid(self):
        """Test list with max value in the middle"""
        max_in_mid = [10, 10, 18, 10, 10]
        self.assertEqual(max_integer(max_in_mid), 18)

    def test_empty_list(self):
        """Test empty List"""
        list = []
        self.assertEqual(max_integer(list), None)

    def test_one_element_in_list(self):
        """Test one Element in a list"""
        list = [1]
        self.assertEqual(max_integer(list), 1)

    def test_negative_values(self):
        """Test negative values"""
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list), -1)

    def test_float_values(self):
        """Test floats value"""
        list = [10.1, 10.2, 10.3, 10.4]
        self.assertEqual(max_integer(list), 10.4)

    def test_list_of_strings(self):
        """Test a string, remember, default was a list but doesn't
        neccessarily it will be a list"""
        string = "Snow"
        self.assertEqual(max_integer(string), 'w')

    def test_list_of_strings(self):
        """Test list of string"""
        list = ["Hi", "I'm", "Snow"]
        self.assertEqual(max_integer(list), "Snow")

    def test_empty_string(self):
        """Test empty strings"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
