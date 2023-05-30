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

    def my_print(self):
        """Print the square with #"""
        [print("#" * self.__size) for i in range(self.__size)]
        if self.__size == 0:
            print()


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()
    print("--")
    my_square.size = 10
    my_square.my_print()
    print("--")
    my_square.size = 0
    my_square.my_print()

    print("--")
