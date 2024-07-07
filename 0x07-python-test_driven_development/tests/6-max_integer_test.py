#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer(list=[])."""

    def test_max_at_end(self):
        """Test for max integer at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_middle(self):
        """Test for max integer in the middle of the list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test for max integer at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_negative_number(self):
        """Test for list with one negative number."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_positive_and_negative(self):
        """Test for mixed positive and negative numbers."""
        self.assertEqual(max_integer([-1, -2, 3, -4]), 3)

    def test_one_element(self):
        """Test for list with one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test for an empty list."""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test for list with float numbers."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_integers_and_floats(self):
        """Test for mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_none_argument(self):
        """Test for None argument."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_argument(self):
        """Test for string argument."""
        with self.assertRaises(TypeError):
            max_integer("string")

    def test_empty_string(self):
        """Test for empty string."""
        self.assertIsNone(max_integer(""))


if __name__ == "__main__":
    unittest.main()
