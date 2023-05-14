#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_num = my_list[0]
    for i in range(len(my_list) - 1):
        if my_list[i + 1] > max_num:
            max_num = my_list[i + 1]
    return max_num
