#!/usr/bin/python3
"""Defines function writes text in a file."""


def write_file(filename="", text=""):
    """
        writes a string to a text file (UTF8) and returns the
        number of characters written.
    """
    with open(filename, mode="w", encoding="utf=8") as f:
        return f.write(text)


if __name__ == "__main__":
    n_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(n_characters)
