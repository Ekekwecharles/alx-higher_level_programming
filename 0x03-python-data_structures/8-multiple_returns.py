#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence += None
        return 0, sentence[0]
    j = 0
    for i in sentence:
        j += 1
    return j, sentence[0]
