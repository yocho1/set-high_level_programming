#!/usr/bin/python3
"""Unittest module for Rectangle class."""
import unittest
import io
import contextlib
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_normal_creation(self):
        r = Rectangle(3, 2, 0, 0, 1)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (3, 2, 0, 0, 1))

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("3", 2)

    def test_width_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-3, 2)

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(3, 2, 1, 1, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/1 - 3/2")

    def test_display(self):
        r = Rectangle(2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_update_args(self):
        r = Rectangle(1, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                          (89, 2, 3, 4, 5))

    def test_update_kwargs(self):
        r = Rectangle(1, 1)
        r.update(width=10, height=20)
        self.assertEqual((r.width, r.height), (10, 20))

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {"id": 5, "width": 10, "height": 2,
                              "x": 1, "y": 9})


if __name__ == "__main__":
    unittest.main()
