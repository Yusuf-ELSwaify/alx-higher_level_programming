#!/usr/bin/python3
"""Defines a text file insert in function."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string.
    """
    text = ""
    with open(filename) as fr:
        for line in fr:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as fw:
        fw.write(text)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
