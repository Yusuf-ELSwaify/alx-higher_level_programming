#!/usr/bin/python3
"""Defines a Python class to JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple class."""
    return obj.__dict__


if __name__ == "__main__":
    MyClass = __import__('8-my_class').MyClass
    class_to_json = __import__('8-class_to_json').class_to_json

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
