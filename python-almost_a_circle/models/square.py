"""Square class that inherits from Rectangle."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class - a Rectangle with equal width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size (same as width/height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size - updates both width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes with args or kwargs."""
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
