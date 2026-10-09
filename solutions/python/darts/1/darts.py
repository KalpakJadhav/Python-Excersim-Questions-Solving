"""Functions to calculate the points scored in a single toss of a Darts game."""

import math


def score(x, y):
    """Calculate the points scored in a single toss of a Darts game.

    Parameters:
        x (float): The x-coordinate of the dart.
        y (float): The y-coordinate of the dart.

    Returns:
        int: The points earned from the dart toss.
    """
    distance = math.hypot(x, y)

    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    return 0