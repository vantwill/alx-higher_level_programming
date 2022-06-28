#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lD = number % 10 if number > 0 else int(repr(number)[-1]) * -1
print("Last digit of {} is {} ".format(number, lD), end="")

if lD > 5:
    print("and is greater than 5")
elif lD == 0:
    print("and is 0")

else:

    print("and is less than 6 and not 0")
