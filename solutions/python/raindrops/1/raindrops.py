"""Module providing a function printing python version."""

import sys


def print_python_version():
    print(sys.version)

def convert(number):
    """Convert a number into its raindrop sounds."""
    result = ""

    if number % 3 == 0:
        result += "Pling"

    if number % 5 == 0:
        result += "Plang"

    if number % 7 == 0:
        result += "Plong"

    if not result:
        result = str(number)

    return result