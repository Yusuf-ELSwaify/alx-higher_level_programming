#!/usr/bin/python3
"""Defines file reading function."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
