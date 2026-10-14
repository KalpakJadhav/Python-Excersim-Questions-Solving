def square_of_sum(number: int) -> int:
    """Calculates the square of the sum of the first N natural numbers."""
    total_sum = (number * (number + 1)) // 2
    return total_sum ** 2


def sum_of_squares(number: int) -> int:
    """Calculates the sum of the squares of the first N natural numbers."""
    return (number * (number + 1) * (2 * number + 1)) // 6


def difference_of_squares(number: int) -> int:
    """Calculates the difference between the square of the sum and the sum of squares."""
    return square_of_sum(number) - sum_of_squares(number)
