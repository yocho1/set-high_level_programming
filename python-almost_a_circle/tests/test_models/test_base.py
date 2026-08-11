#!/usr/bin/python3
"""Unittest module for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the object counter before every test."""
        Base._Base__nb_objects = 0

    def test_id_none(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_public(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_id_default_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_type_str(self):
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_id_type_float(self):
        b = Base(3.14)
        self.assertEqual(b.id, 3.14)


if __name__ == "__main__":
    unittest.main()
