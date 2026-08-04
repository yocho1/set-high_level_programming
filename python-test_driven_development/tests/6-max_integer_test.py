#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max of a list already in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max of a list not in any particular order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Max of a list in descending order."""
        self.assertEqual(max_integer([9, 7, 5, 3, 1]), 9)

    def test_single_element(self):
        """Max of a list with only one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Max of an empty list is None."""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """Calling with no argument uses the default empty list."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Max of a list containing only negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3, -10]), -1)

    def test_mixed_positive_and_negative(self):
        """Max of a list mixing positive and negative numbers."""
        self.assertEqual(max_integer([-10, 5, -3, 8, 0]), 8)

    def test_all_same_values(self):
        """Max of a list where every element is identical."""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_max_at_start(self):
        """Max value located at the start of the list."""
        self.assertEqual(max_integer([100, 1, 2, 3]), 100)

    def test_max_at_end(self):
        """Max value located at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 100]), 100)

    def test_max_in_middle(self):
        """Max value located in the middle of the list."""
        self.assertEqual(max_integer([1, 100, 2, 3]), 100)

    def test_floats_in_list(self):
        """Max of a list containing floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_two_elements(self):
        """Max of a list with exactly two elements."""
        self.assertEqual(max_integer([2, 8]), 8)
        self.assertEqual(max_integer([8, 2]), 8)


if __name__ == '__main__':
    unittest.main()
