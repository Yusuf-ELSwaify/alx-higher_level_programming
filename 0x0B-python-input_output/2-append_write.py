#!/usr/bin/python3
"""Defines function appends text in a file."""


def append_write(filename="", text=""):
    """
        appends a string at the end of a text file (UTF8)
        and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    n_characters_added = append_write("file_append.txt",
                                      "This School is so cool!\n")
    print(n_characters_added)
