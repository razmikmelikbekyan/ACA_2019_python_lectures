from math import sin


def square(x: int or float) -> int or float:
    """Calculates the square of given value."""
    return x * x


def triangle_area(x: int or float, y: int or float, alpha: int or float) -> float:
    """Calculates the triangle area using given 2 sides and their angle."""
    return x * y * sin(alpha) / 2


def triangle_perimeter(x: int or float, y: int or float, z: int or float) -> int or float:
    """Calculates the triangle perimeter using given sides of triangle."""
    return x + y + z
