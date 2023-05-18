#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev = 0

    for i in roman_string[::-1]:
        value = romans.get(i, 0)
        if value == 0:
            return 0
        res += value * (1 if prev <= value else -1)
        prev = value
    return res
