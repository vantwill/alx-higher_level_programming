#!/usr/bin/python3
# 102-magic_calculation.py
def magic_calculation(a, b):
    result = 0
    for t in range(1, 3):
        try:
            if t > a:
                raise Exception('Too far')
            else:
                result += a ** b / t
        except:
            result = b + a
            break
    return (result)
