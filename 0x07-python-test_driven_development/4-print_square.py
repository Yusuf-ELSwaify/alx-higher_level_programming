#!/usr/bin/python3
"""defines a function to print square."""


def print_square(size):
    """print a square of size <size> with #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [print("#" * size) for _ in range(size)]
