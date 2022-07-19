#!/usr/bin/python3
"1-square.py define"


class Square:
    """Class Square
    """

    def __init__(self, size=0):
        """square class love me
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """squre class are  best class all are equal
        """
        return self.__size ** 2
