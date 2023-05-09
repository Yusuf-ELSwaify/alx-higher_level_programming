#!/usr/bin/python3
i = 32
for c in range(ord('Z'), ord('A') - 1, -1):
    print("{}".format(chr(c + i)), end="")
    i = 0 if i == 32 else 32
