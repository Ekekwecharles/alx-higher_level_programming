#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    m = -number
    if m > 9:
        m = m % 10
    if m == 0:
        print(f"Last digit of {number} is {m} and is 0")
    else:
        m = -m
        print(f"Last digit of {number} is {m} and is less than 6 and not 0")
elif number > 0:
    m = number
    if m > 9:
        m = m % 10
    if m > 5:
        print(f"Last digit of {number} is {m} and is greater than 5")
    elif m < 6 and m != 0:
        print(f"Last digit of {number} is {m} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {m} and is 0")
