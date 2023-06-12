#!/usr/bin/python3
"""Define type checking function"""


def is_same_class(obj, a_class):
    """Check if an object is an type of a given class."""
    if type(obj) == a_class:
        return True
    return False


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
