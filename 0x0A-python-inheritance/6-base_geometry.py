#!/usr/bin/python3
"""Define class BaseGeometry."""


class BaseGeometry:
    """Blueprint for a BaseGeometry."""
    def area(self):
        """Not implemented yet function."""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
