#!/usr/bin/python3
def remove_char_at(str, n):
    char = ""
    j = 0
    for i in str:
        if j == n:
            j += 1
            continue
        char += i
        j += 1
    return char
