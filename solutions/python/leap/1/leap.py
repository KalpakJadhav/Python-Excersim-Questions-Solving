"""Functions to determine if a year is a leap year."""


def leap_year(year):
    """Determine if a year is a leap year.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: Is the year a leap year?
    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)