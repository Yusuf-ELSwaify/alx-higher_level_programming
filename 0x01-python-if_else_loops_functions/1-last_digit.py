#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number - (int(number / 10) * 10)

print(f"Last digit of {number:d} is {digit:d} and is", end=" ")
if digit == 0:
    print("0")
elif digit > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
