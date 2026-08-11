#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_is_rectangle_subclass(self):
        s = Square(5)
        self.assertIsInstance(s, Rectangle)

    def test_size_sets_width_height(self):
        s = Square(5)
        self.assertEqual((s.width, s.height), (5, 5))

    def test_str(self):
        s = Square(5, 1, 1, 8)
        self.assertEqual(str(s), "[Square] (8) 1/1 - 5")

    def test_update_size(self):
        s = Square(5)
        s.update(size=10)
        self.assertEqual((s.width, s.height), (10, 10))


if __name__ == "__main__":
    unittest.main()
