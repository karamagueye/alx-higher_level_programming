#!/usr/bin/python3
"""Square module"""


class Square:
    """Defines a square."""


    def __init__(self, size=0):
        """constructure.


        Args:
            size: Length of a side of the square.


           Raises:
               TypeError: if size is not an interger
               ValueError: if size is less than 0
           """
            if not isinstance(size, int):
                raise TypeError('size must be an interger')
            if size < 0:
                raise ValueError('size must be >= 0')
            self.__size = size
