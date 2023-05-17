#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None
    _max = 0
    for k, v in a_dictionary.items():
        if a_dictionary[k] > _max:
            _max = a_dictionary[k]
            key = k
    return key
