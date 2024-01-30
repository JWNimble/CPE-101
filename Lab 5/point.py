class Point:
    """Represents a point in 2D space
    Attributes:
        x (float): x coordinate index
        y (float): y coordinate
    """

    def __init__(self, x:float, y:float):
        """The initializer for a point object
        Args:
            x (float) = x
            y (float) = y
        """

        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
