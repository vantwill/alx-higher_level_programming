#!/usr/bin/python3
# 102-magic_calculation.py
def magic_calculation(a, b):
    reslt = 0
    for t in range(1, 3):
        try:
            if t > a:
                raise Exception('Too far')
            else:
                reslt += a ** b / t
        except:
            reslt = b + a
            break
    return (reslt)
