#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    count = len(sys.argv) - 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = ['+', '-', '*', '/']
    argv = sys.argv
    if argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == '+':
        print(f"{a} + {b} = {add(a, b)}")
    elif argv[2] == '-':
        print(f"{a} - {b} = {sub(a, b)}")
    elif argv[2] == '*':
        print(f"{a} * {b} = {mul(a, b)}")
    elif argv[2] == '/':
        print(f"{a} / {b} = {div(a, b)}")
