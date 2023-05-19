#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    my_dict = dict(my_list)
    val, val1 = 0, 0
    for k, v in my_dict.items():
        val += k * v
        val1 += v
    return val / val1
