#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Blueprint for a square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set Square size.

        Args:
            value (int): The new value of size of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the Square ==."""
        return self.__size == other.__size

    def __ne__(self, other):
        """Define the Square !=."""
        return self.__size != other.__size

    def __lt__(self, other):
        """Define the Square <."""
        return self.__size < other.__size

    def __gt__(self, other):
        """Define the Square >."""
        return self.__size > other.__size

    def __le__(self, other):
        """Define the Square <=."""
        return self.__size <= other.__size

    def __ge__(self, other):
        """Define the Square >=."""
        return self.__size >= other.__size


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
