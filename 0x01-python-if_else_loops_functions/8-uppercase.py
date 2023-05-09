#!/usr/bin/python3
def uppercase(str):
    output = ""
    for i in str:
        if i >= 'a' and i <= 'z':
            j = chr(ord(i) - ord('a') + ord('A'))
            output += j
        else:
            output += i
    print("{}".format(output))
