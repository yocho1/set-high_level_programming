t tests for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_id_assignment(self):
        """Test that id is assigned correctly."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_id_none(self):
        """Test that id increments correctly."""
        b1 = Base(None)
        self.assertEqual(b1.id, 4)

        b2 = Base(None)
        self.assertEqual(b2.id, 5)

    def test_id_string(self):
        """Test with string id."""
        b1 = Base("test")
        self.assertEqual(b1.id, "test")

    def test_id_float(self):
        """Test with float id."""
        b1 = Base(3.14)
        self.assertEqual(b1.id, 3.14)


if __name__ == "__main__":
    unittest.main()
