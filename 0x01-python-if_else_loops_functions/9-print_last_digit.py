def print_last_digit(number):
    lastDigit = abs(number - (int(number / 10) * 10))
    print(lastDigit, end="")
    return lastDigit
