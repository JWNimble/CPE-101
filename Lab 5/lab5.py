"""
CPE101
Spring 2021
Author: Jack Forrester
"""

from point import Point
from circle import Circle
import turtle

def euclid_distance(a, b)->float:
    """Computes Euclidean distance
    Args:
        a (Point): a point
        b (Point): another point
    Returns:
        float: the euclidean distance between the points
    """

    d = ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
    
    return round(d, 2)


def overlap(circle1:Circle, circle2:Circle)->bool:
    """Checks if two circles overlap each other
    Args:
        circle1 (Circle): a circle
        circle2 (Circle): another circle
    Returns:
        bool: True if the circles do overlap eachother and false if they do not
    """

    center_dif = euclid_distance(circle1.center, circle2.center)
    radius_sum = circle1.radius + circle2.radius

    return center_dif <= radius_sum


def draw_circle(turtle, circle):
    bob.penup()
    bob.setx(circle.center.x)
    bob.sety(circle.center.y)
    bob.pendown()
    bob.circle(circle.radius)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    p1 = Point(0, 0)
    p2 = Point(7, 4)
    cir1 = Circle(p1, 2)
    cir2 = Circle(p1, 2)
    cir3 = Circle(p2, 6)
    bob = turtle.Turtle()
    draw_circle(bob, cir3)
    turtle.done()
    print(euclid_distance(p1, p2))
    print(overlap(cir1, cir2))
    print(overlap(cir1, cir3))
    assert repr(p1 == 'Point(x=0, y=0)')
    assert (cir1 == cir2) == True
    assert (cir1 == cir3) == False
    assert (cir2 == cir3) == False

