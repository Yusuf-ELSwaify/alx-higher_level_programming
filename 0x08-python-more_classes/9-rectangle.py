#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Blueprint for a rectangle
    Attributes:
        number_of_instances (int): rectangle instances number.
        print_symbol (any): The symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set rectangle width.

        Args:
            value (int): The new value of width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set rectangle height.

        Args:
            value (int): The new value of height of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def area(self):
        """Return the rectangle area."""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character."""
        rect_str = [str(self.print_symbol) * self.__width
                    for i in range(self.__height if self.__width else 0)]
        return '\n'.join(rect_str)

    def __repr__(self):
        """Return the string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for the deletion of a rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with greater area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new rectangle that width and height = size.

        Args:
            size (int): The width and height of the new rectangle.
        """
        return cls(size, size)


if __name__ == "__main__":
    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}"
          .format(my_square.area(), my_square.perimeter()))
    print(my_square)
