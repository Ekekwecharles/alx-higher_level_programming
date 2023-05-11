#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    total_sum = 0
    for i in argv[1:]:
        num = int(i)
        total_sum += num
    print(f"{total_sum}")
