"""This is my dummy module"""
import os


def dummyfunc():
    """This is my dummy function.

    Returns:
        int: Always returns one.
    """
    print(1 + 1)
    print(os.getcwd())
    myCamelVar = 5
    print(myCamelVar)
    return 1


def myfunc(a, b, c, d):
    print(a + b + c + d)
    print("hello")
