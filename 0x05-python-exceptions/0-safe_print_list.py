#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
        except IndexError:
            i -= 1
            break
    print()
    return i + 1
