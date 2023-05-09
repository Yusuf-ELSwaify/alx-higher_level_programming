#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int((abs(number) % 10) * (number / abs(number)))

print(f"Last digit of {number:d} is {digit:d} and is", end=" ")
if digit == 0:
    print("0")
if digit > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
