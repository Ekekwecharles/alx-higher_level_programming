#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in my_list:
            if x > 0:
                print(f"{i}", end="")
                j += 1
                x -= 1
                continue
            break
    except Exception:
        pass
    finally:
        print()
    return j
