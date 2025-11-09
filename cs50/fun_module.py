# Written by: Charles Underwood
# Interpretied: Python module.py
# This file exists to keep my code tidy and organized.

import numpy as np
import random as rnd
import math as math
import matplotlib.pyplot as plt


def sqrt(x):
    return x**0.5


def square(x):
    return x**2


def nth_power(x, n):
    return x**n


def nth_root(x, n):
    return x ** (1 / n)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def power(x, y):
    return x**y
