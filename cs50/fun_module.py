# Written by: Charles Underwood
# Interpretied: Python module.py
# This file exists to keep my code tidy and organized.

import random as rnd
import math as math


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


def main():
    complete = 0
    while complete != 1:
        print("Hello, world!")

        # complete
        complete = 1

        # Complete the program
        if complete == 1:
            print("Program completed successfully.")
        else:
            print("Program not completed.")
            continue
        break


main()  # Call the main function to start the program.
