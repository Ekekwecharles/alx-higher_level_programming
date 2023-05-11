#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argvv = sys.argv
    count = len(argvv) - 1
    if count == 0:
        print("0 arguments.")
    else:
        if count == 1:
            print("1 argument:")
        else:
            print(f"{count} arguments:")
        j = 0
        for i in argvv:
            if j == 0:
                j += 1
                continue
            print(f"{j}: {i}")
            j += 1
