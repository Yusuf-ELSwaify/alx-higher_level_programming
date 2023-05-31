#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Blueprint for a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                any(not isinstance(num, int) or num < 0
                    for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                any((not isinstance(num, int) or num < 0)
                    for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set Square position.

        Args:
            value (int): The new value of position of the square.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                any(not isinstance(num, int) or num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with #"""
        [print(((" " * self.__position[0]) + "#" * self.__size)
               if i >= self.__position[1] else "")
            for i in range(self.__size + self.__position[1])]
        if self.__size == 0:
            print()

    def __str__(self):
        """Print the square with #"""
        draw_size = self.__size + self.__position[1]
        square_str = "".join((((" " * self.__position[0]) + "#" * self.__size
                               if i >= self.__position[1] else "") +
                              ("\n" if (i < (draw_size - 1)) else ""))
                             for i in range(draw_size
                                            if (self.__size != 0) else 0))
        return square_str


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
