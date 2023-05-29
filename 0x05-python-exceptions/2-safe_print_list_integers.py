#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    j = 0
    num = 0
    try:
        while j < x:
            if not isinstance(my_list[j], int):
                j += 1
                continue
            print("{:d}".format(my_list[j]), end="")
            j += 1
            num += 1
        print()
        return num
    except Exception:
        raise
