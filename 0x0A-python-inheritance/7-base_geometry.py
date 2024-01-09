#!/usr/bin/python3
"""Define"""
class BaseGeometry:
    """ represent bvasre geometry"""
    def area(self):
        """Not yet implement"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """value a parameter as an integer"""
        if type(value) != int:
            raise TypeError("{}must be an interger"format(name))
        if value <= 0:
            raise ValueError("{} must be freater tfhan 0".format(name))
