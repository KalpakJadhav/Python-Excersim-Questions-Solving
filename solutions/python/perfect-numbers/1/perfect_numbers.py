def classify(number):
    """A perfect number equals the sum of its positive divisors."""

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    divisors_sum = sum(
        divisor
        for divisor in range(1, number)
        if number % divisor == 0
    )

    if divisors_sum == number:
        return "perfect"
    elif divisors_sum > number:
        return "abundant"
    else:
        return "deficient"