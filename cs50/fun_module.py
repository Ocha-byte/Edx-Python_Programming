# Written by Charles Underwood
# This module exists to keep my code tidy and organized.

import numpy as np
import random as rnd
import math as math
import matplotlib.pyplot as plt
import datetime as dt


# Pre-allocation
result = 0

# Variables
rdigit = rnd.randrange(1, 15)
pi = math.pi
ct = dt.datetime.now()
numMonth = float(12)
currentMonth = ct.month

pi_digits = (
    1,
    4,
    1,
    5,
    9,
    2,
    6,
    5,
    3,
    5,
    8,
    9,
    7,
    9,
    3,
)  # A tuple of digits of pi


def hello_user():
    name = input("What's your name? ").strip().title()
    print(f"Hello, {name}!")


def cmonth():
    print("There are", numMonth, "months in a year")
    print("The current month is", currentMonth)


def plotting():
    x = float(input("Enter a number: "))
    y = float(2 * np.cos(x))
    print(f"(x,y) = ({x}, {y})")
    plt.plot(x, y)
    plt.show()


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


def perform_arithmetic(x, y, operation):
    if operation == "+":
        return add(x, y)
    elif operation == "-":
        return subtract(x, y)
    elif operation == "*":
        return multiply(x, y)
    elif operation == "/":
        return divide(x, y)
    elif operation == "^":
        return power(x, y)
    else:
        raise ValueError("Invalid operation")


def arithmetic_operations():
    x = float(input("Enter a number: "))
    y = float(input("Enter another number: "))
    operation = input("Enter operation (+, -, *, /, ^): ")
    result = perform_arithmetic(x, y, operation)
    print(f"{x} {operation} {y} = {result}")


def sqrt(x):
    return x**0.5


def square(x):
    return x**2


def nth_power(x, n):
    return x**n


def nth_root(x, n):
    return x ** (1 / n)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def perform_powers(x, operation):
    if operation == "sqrt":
        return sqrt(x)
    elif operation == "square":
        return square(x)
    elif operation == "nth_power":
        n = int(input("Enter the power: "))
        return nth_power(x, n)
    elif operation == "nth_root":
        n = int(input("Enter the root: "))
        return nth_root(x, n)
    elif operation == "factorial":
        return factorial(x)
    else:
        print("Invalid operation")


def powers():
    x = float(input("Enter a number: "))
    operation = input(
        "Enter operation (sqrt, square, nth_power, nth_root, factorial): "
    )
    result = perform_powers(x, operation)
    print(f"{operation}({x}) = {result}")


def divider():
    n = int(input("Enter the divisor: "))
    is_divisible_by_n = pi_digits[rdigit] % n == 0
    print("Is divisible by", n, ":", is_divisible_by_n)


def pos_or_neg():
    x = float(input("Enter a number: "))
    if x > 0:
        print(f"{x} is positive")
    elif x < 0:
        print(f"{x} is negative")
    else:
        print(f"{x} is zero")


def fruity_array():
    fruit1, fruit2, fruit3 = "apple", "banana", "orange"
    fruit4 = fruit5 = fruit6 = "lime"
    fruits = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6]
    print(fruits[0])
    print(fruits[1])
    print(fruits[2])
    print(fruits[0] + fruits[1] + fruits[2])
    print(fruits[3] + fruits[4] + fruits[5])


def polar_plot(Re, Im):
    r = np.sqrt(Re**2 + Im**2)
    theta = np.arctan2(Im, Re)
    plt.polar(r, theta)
    plt.show()


def cartesian_plot(Re, Im):
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = X + Y * 1j
    plt.contourf(X, Y, np.abs(Z - (Re + Im * 1j)), cmap="viridis")
    plt.colorbar()
    plt.show()


def three_d_plot(Re, Im):
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = X + Y * 1j
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, np.abs(Z - (Re + Im * 1j)), cmap="viridis")
    plt.show()


def perform_complex(Re, Im, Op):
    if Op == "+":
        print(f"The sum is: {Re + Im * 1j + Re + Im * 1j}")
    elif Op == "-":
        print(f"The difference is: {Re + Im * 1j - Re + Im * 1j}")
    elif Op == "*":
        print(f"The product is: {Re + Im * 1j * Re + Im * 1j}")
    elif Op == "/":
        print(f"The quotient is: {Re + Im * 1j / Re + Im * 1j}")
    elif Op == "polar":
        print(f"The polar representation is: {abs(Re + Im * 1j)}")
    elif Op == "cartesian":
        print(f"The Cartesian representation is: {Re + Im * 1j}")
    elif Op == "conjugate":
        print(f"The conjugate is: {Re + Im * 1j.conjugate()}")
    elif Op == "plot":
        type = input(
            "What type of plot? Polar, Cartesian, both, or 3D? (p, c, b, 3d): "
        )
        if type == "p":
            print(f"Polar plot of {Re + Im * 1j}")
            polar_plot(Re, Im)
        elif type == "c":
            print(f"Cartesian plot of {Re + Im * 1j}")
            cartesian_plot(Re, Im)
        elif type == "b":
            print(f"Both plots of {Re + Im * 1j}")
            polar_plot(Re, Im)
            cartesian_plot(Re, Im)
        elif type == "3d":
            print(f"3D plot of {Re + Im * 1j}")
            three_d_plot(Re, Im)
        else:
            print("Invalid plot type")
    else:
        print("Invalid operation")


def complex_numbers():
    Re = float(input("Enter a real number: "))
    Im = float(input("Enter an imaginary number: "))
    print(f"The complex number is: {Re + Im * 1j}")
    Op = input("Enter an operation (+, -, *, /, polar, cartesian, conjugate, plot): ")
    perform_complex(Re, Im, Op)


def perform_bit_ops(bit0, bit1, Op):
    if Op == "and":
        print(f"AND operation of {bit0} and {bit1}: {bit0 and bit1}")
    elif Op == "or":
        print(f"OR operation of {bit0} and {bit1}: {bit0 or bit1}")
    elif Op == "xor":
        print(f"XOR operation of {bit0} and {bit1}: {bit0 ^ bit1}")
    elif Op == "left shift":
        print(f"Left shift operation of {bit0} by {bit1}: {bit0 << bit1}")
    elif Op == "right shift":
        print(f"Right shift operation of {bit0} by {bit1}: {bit0 >> bit1}")
    elif Op == "left rotate":
        print(
            f"Left rotate operation of {bit0} by {bit1}: {bit0 << bit1 | bit0 >> (8 - bit1)}"
        )
    elif Op == "right rotate":
        print(
            f"Right rotate operation of {bit0} by {bit1}: {bit0 >> bit1 | bit0 << (8 - bit1)}"
        )
    elif Op == "bitwise and":
        print(f"Bitwise AND operation of {bit0} and {bit1}: {bit0 & bit1}")
    elif Op == "bitwise or":
        print(f"Bitwise OR operation of {bit0} and {bit1}: {bit0 | bit1}")
    elif Op == "bitwise xor":
        print(f"Bitwise XOR operation of {bit0} and {bit1}: {bit0 ^ bit1}")
    elif Op == "bitwise not":
        print(f"Bitwise NOT operation of {bit0}: {~bit0}")
    else:
        print("Invalid operation")


def bit_ops():
    bit0 = bool(input("Enter bit value: (0 or 1): "))
    bit1 = bool(input("Enter bit value: (0 or 1): "))
    Op = input(
        "Enter operation: (and, or, xor, left shift, right shift, left rotate, right rotate, bitwise and, bitwise or, bitwise xor): "
    )
    perform_bit_ops(bit0, bit1, Op)


def half_adder(x, y):
    sum = x ^ y
    carry = x & y
    return sum, carry


def full_adder(x, y, carry):
    sum1, carry1 = half_adder(x, y)
    sum2, carry2 = half_adder(sum1, carry)
    carry3 = carry1 | carry2
    return sum2, carry3


def adders():
    a = bool(input("Enter a number (0 or 1): "))
    b = bool(input("Enter a number (0 or 1): "))
    sum, carry = half_adder(a, b)
    result, carry = full_adder(sum, carry, False)
    print("Result:", result)
    print("Carry:", carry)


def rnd_pi():
    pi_array = str(pi).split(".")[1]
    print("The", rdigit + 1, "digit of pi is", pi_array[rdigit])
    print("Is equal:", pi_array[rdigit] is not pi_digits[rdigit])


def check_prime():
    num = float(input("Enter a number: "))
    if num <= 1:
        print("No, it is not a prime number.")
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("No, it is not a prime number.")
        print("Yes, it is a prime number.")


def odd_evens():
    num = float(input("Enter a number: "))
    is_even = num % 2 == 0
    is_odd = num % 2 != 0
    print("Is even:", is_even)
    print("Is odd:", is_odd)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def op_s():
    print("The operation was successful.")
