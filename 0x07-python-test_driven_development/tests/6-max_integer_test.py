#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """testcases of max_integer()."""
    def test_ordered_list(self):
        """Test an ordered list of integers."""
        list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(list), 5)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        list = [1, 4, 5, 3, 1]
        self.assertEqual(max_integer(list), 5)

    def test_negative_numbers_list(self):
        """Test negative numbers list."""
        list = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(list), -1)

    def test_single_number_list(self):
        """Test negative numbers list."""
        list = [1]
        self.assertEqual(max_integer(list), 1)

    def test_duplicate_list(self):
        """Test duplicate list."""
        list = [1, 1, 2, 2, 3, 3]
        self.assertEqual(max_integer(list), 3)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        list = [1.0, 2.2, 3.5, 4.4, 5.8]
        self.assertEqual(max_integer(list), 5.8)

    def test_empty(self):
        """test an empty list"""
        list = []
        self.assertIsNone(max_integer(list))
