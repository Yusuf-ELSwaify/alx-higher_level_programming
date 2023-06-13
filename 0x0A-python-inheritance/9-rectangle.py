#!/usr/bin/python3
"""Define class Rectangle inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Blueprint for a rectangle"""
    def __init__(self, width, height):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation for Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
