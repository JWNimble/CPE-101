from point import Point


class Circle:
    """Represents a circle in 2D space
    Attributes:
        center (Point): a point which serves as the center of the circle
        radius (float): distance from the center to the circles outer edge
    """

    def __init__(self, center:Point, radius:int):
        """The initializer for the Circle object.
        Args:
            center (Point) = center
            radius (int) = radius
        """

        self.radius = radius
        self.center = center

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

    def __eq__(self, other):
        return isinstance(other, Circle) and self.center == other.center and self.radius == other.radius
