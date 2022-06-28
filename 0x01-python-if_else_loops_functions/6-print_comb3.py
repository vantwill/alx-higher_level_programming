#!/usr/bin/python3
for k in range(10):

    for j in range(k + 1, 10):
        print(
            "{}{}".format(k, j),

            end=", " if int(str(k) + str(j)) < 89 else "\n"
            )
