#!/usr/bin/python3
"""defines a function to sum two integers."""


def add_integer(a, b=98):
    """Return the summation of a and b
    Raises:
        TypeError: If a or b is a not an integer and not a float.
    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")

    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
