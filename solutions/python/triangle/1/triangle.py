"""Functions to determine if a triangle is equilateral, isosceles, or scalene."""


def is_valid_triangle(sides):
    """Check if the given sides form a valid triangle."""
    a, b, c = sides
    # All sides must be strictly greater than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Triangle inequality theorem
    if (a + b < c) or (b + c < a) or (a + c < b):
        return False
    return True


def equilateral(sides):
    """Determine if a triangle is equilateral.

    An equilateral triangle has all three sides the same length.
    """
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b == c


def isosceles(sides):
    """Determine if a triangle is isosceles.

    An isosceles triangle has at least two sides the same length.
    """
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a == b or b == c or a == c


def scalene(sides):
    """Determine if a triangle is scalene.

    A scalene triangle has all sides of different lengths.
    """
    if not is_valid_triangle(sides):
        return False
    a, b, c = sides
    return a != b and b != c and a != c