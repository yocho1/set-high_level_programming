#!/usr/bin/python3
"""Unittest module for Rectangle class."""
import unittest
import io
import os
import contextlib
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    # ---- construction ----
    def test_width_height(self):
        r = Rectangle(1, 2)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 0, 0))

    def test_width_height_x(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 0))

    def test_width_height_x_y(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_all_args_type_error_width(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_all_args_type_error_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_all_args_type_error_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_all_args_type_error_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_width_height_x_y_id(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id), (1, 2, 3, 4, 5))

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    # ---- area / str / display ----
    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        r = Rectangle(3, 2, 1, 1, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/1 - 3/2")

    def test_display_no_x_no_y(self):
        r = Rectangle(2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        r = Rectangle(2, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "  ##\n  ##\n")

    def test_display_x_and_y(self):
        r = Rectangle(2, 2, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {"id": 5, "width": 10, "height": 2,
                              "x": 1, "y": 9})

    # ---- update(*args) ----
    def test_update_no_args(self):
        r = Rectangle(1, 1)
        r.update()
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 1, 0, 0))

    def test_update_id(self):
        r = Rectangle(1, 1)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_id_width(self):
        r = Rectangle(1, 1)
        r.update(89, 1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_id_width_height(self):
        r = Rectangle(1, 1)
        r.update(89, 1, 2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_id_width_height_x(self):
        r = Rectangle(1, 1)
        r.update(89, 1, 2, 3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_id_width_height_x_y(self):
        r = Rectangle(1, 1)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                          (89, 1, 2, 3, 4))

    # ---- update(**kwargs) ----
    def test_update_kwargs_id(self):
        r = Rectangle(1, 1)
        r.update(id=89)
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        r = Rectangle(1, 1)
        r.update(id=89, width=1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_update_kwargs_id_width_height(self):
        r = Rectangle(1, 1)
        r.update(id=89, width=1, height=2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_update_kwargs_id_width_height_x(self):
        r = Rectangle(1, 1)
        r.update(id=89, width=1, height=2, x=3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_update_kwargs_id_width_height_x_y(self):
        r = Rectangle(1, 1)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                          (89, 1, 2, 3, 4))

    # ---- create() ----
    def test_create_id_only(self):
        r = Rectangle.create(id=89)
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        r = Rectangle.create(id=89, width=1)
        self.assertEqual((r.id, r.width), (89, 1))

    def test_create_id_width_height(self):
        r = Rectangle.create(id=89, width=1, height=2)
        self.assertEqual((r.id, r.width, r.height), (89, 1, 2))

    def test_create_id_width_height_x(self):
        r = Rectangle.create(id=89, width=1, height=2, x=3)
        self.assertEqual((r.id, r.width, r.height, r.x), (89, 1, 2, 3))

    def test_create_id_width_height_x_y(self):
        r = Rectangle.create(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual((r.id, r.width, r.height, r.x, r.y),
                          (89, 1, 2, 3, 4))

    # ---- save_to_file / load_from_file ----
    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_list(self):
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"width": 1', content)

    def test_load_from_file_no_file(self):
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_existing(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].to_dictionary(), r.to_dictionary())


if __name__ == "__main__":
    unittest.main()
