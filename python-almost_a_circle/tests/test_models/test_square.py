#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_is_rectangle_subclass(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_size_only(self):
        s = Square(1)
        self.assertEqual((s.width, s.height, s.x, s.y), (1, 1, 0, 0))

    def test_size_x(self):
        s = Square(1, 2)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 0))

    def test_size_x_y(self):
        s = Square(1, 2, 3)
        self.assertEqual((s.size, s.x, s.y), (1, 2, 3))

    def test_size_x_y_id(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual((s.size, s.x, s.y, s.id), (1, 2, 3, 4))

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(5, 1, 1, 8)
        self.assertEqual(str(s), "[Square] (8) 1/1 - 5")

    def test_to_dictionary(self):
        s = Square(5, 1, 1, 8)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": 8, "size": 5, "x": 1, "y": 1})

    # ---- update(*args) ----
    def test_update_no_args(self):
        s = Square(1)
        s.update()
        self.assertEqual(s.size, 1)

    def test_update_id(self):
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_id_size(self):
        s = Square(1)
        s.update(89, 1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_id_size_x(self):
        s = Square(1)
        s.update(89, 1, 2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_id_size_x_y(self):
        s = Square(1)
        s.update(89, 1, 2, 3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    # ---- update(**kwargs) ----
    def test_update_kwargs_id(self):
        s = Square(1)
        s.update(id=89)
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        s = Square(1)
        s.update(id=89, size=1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_update_kwargs_id_size_x(self):
        s = Square(1)
        s.update(id=89, size=1, x=2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_update_kwargs_id_size_x_y(self):
        s = Square(1)
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    # ---- create() ----
    def test_create_id_only(self):
        s = Square.create(id=89)
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        s = Square.create(id=89, size=1)
        self.assertEqual((s.id, s.size), (89, 1))

    def test_create_id_size_x(self):
        s = Square.create(id=89, size=1, x=2)
        self.assertEqual((s.id, s.size, s.x), (89, 1, 2))

    def test_create_id_size_x_y(self):
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual((s.id, s.size, s.x, s.y), (89, 1, 2, 3))

    # ---- save_to_file / load_from_file ----
    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_list(self):
        s = Square(1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertIn('"size": 1', content)

    def test_load_from_file_no_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_existing(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].to_dictionary(), s.to_dictionary())


if __name__ == "__main__":
    unittest.main()
