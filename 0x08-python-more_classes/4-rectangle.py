#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Blueprint for a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
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
        rect_str = ["#" * self.__width
                    for i in range(self.__height if self.__width else 0)]
        return '\n'.join(rect_str)

    def __repr__(self):
        """Return the string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
    my_rectangle = Rectangle(0, 0)
    print("Area: {} - Perimeter: {}"
          .format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")
    my_rectangle = Rectangle(0, 4)
    print("Area: {} - Perimeter: {}"
          .format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))

    print("--")
    my_rectangle = Rectangle(4, 0)
    print("Area: {} - Perimeter: {}"
          .format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
