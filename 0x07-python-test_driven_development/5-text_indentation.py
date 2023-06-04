#!/usr/bin/python3
"""defines a function to print text with indentation."""


def text_indentation(text):
    """prints a text with 2 new lines after these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delimeters = ".?:"
    lines = []
    line = ""
    for c in text:
        line += c
        if c in delimeters:
            lines.append(line.strip(" "))
            lines.append("")
            line = ""
    lines.append(line.strip(" "))
    print("\n".join(lines), end="")
