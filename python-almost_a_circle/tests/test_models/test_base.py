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

    def test_id_default_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_public(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_list(self):
        result = Base.to_json_string([{'id': 12}])
        self.assertEqual(result, '[{"id": 12}]')

    def test_to_json_string_returns_str(self):
        result = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(result, str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_with_data(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_string_returns_list(self):
        result = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
