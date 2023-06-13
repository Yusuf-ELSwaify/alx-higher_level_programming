#!/usr/bin/python3
"""Define class Square inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Blueprint for a square"""
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the square area"""
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of the square"""
        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
