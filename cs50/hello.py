#
# Course: CS50's Introduction to Programming with Python
# Comppletion Time: 1.783 hrs, 31 October 2025.
# Interpretied: Python hello.py
# This contains code from the course and my own.
#

import fun_module as fun

import numpy as np
import random as rnd
import math as math
import matplotlib.pyplot as plt


def main():
    complete = 0
    while complete != 1:
        print("")
        print("Which program would you like to run?")
        print("1. Hello World")
        print("2. Hello User")
        print("3. Casting Months")
        print("4. Plotting")
        print("5. Arithmetic Operations")
        print("6. Powers")
        print("7. Odd Even")
        print("8. Positive Negative Zero")
        print("9. Fruity Arrays")
        print("10. Complex Numbers")
        print("11. Bit Operations")
        print("12. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Hello world!")
        elif choice == "2":
            name = input("What's your name? ").strip().title()
            print(f"Hello, {name}!")
        elif choice == "3":
            currentMonth = 11
            Month = float(12)
            print(type(Month))
            print("There are", Month, "months in a year")
            print("The current month is", currentMonth)
        elif choice == "4":
            x = input("Enter a number: ")
            x = float(x)
            y = 2 * np.cos(x)
            y = float(y)
            print(f"(x,y) = ({x}, {y})")
            plt.plot(x, y)
            plt.show()
        elif choice == "5":
            x = float(input("Enter a number: "))
            y = float(input("Enter another number: "))
            operation = input("Enter operation (+, -, *, /, ^): ")
            if operation == "+":
                result = fun.add(x, y)
            elif operation == "-":
                result = fun.sub(x, y)
            elif operation == "*":
                result = fun.mul(x, y)
            elif operation == "/":
                result = fun.div(x, y)
            elif operation == "^":
                result = fun.pow(x, y)
            else:
                print("Invalid operation")
            print(f"{x} {operation} {y} = {result}")
            print("Operation completed")
        elif choice == "6":
            x = float(input("Enter a number: "))
            operation = input(
                "Enter operation (sqr, square, nth_power, nth_root, factorial): "
            )
            if operation == "sqr":
                result = fun.sqr(x)
            elif operation == "square":
                result = fun.square(x)
            elif operation == "nth_power":
                n = int(input("Enter the power: "))
                result = fun.nth_power(x, n)
            elif operation == "nth_root":
                n = int(input("Enter the root: "))
                result = fun.nth_root(x, n)
            elif operation == "factorial":
                result = fun.factorial(x)
            else:
                print("Invalid operation")
            print(f"{operation}({x}) = {result}")
            print("Operation completed")
        elif choice == "7":
            x = float(input("Enter a number: "))
            if x % 2 == 0:
                print(f"{x} is even")
            else:
                print(f"{x} is odd")
                print("Operation completed")
        elif choice == "8":
            x = float(input("Enter a number: "))
            if x > 0:
                print(f"{x} is positive")
            elif x < 0:
                print(f"{x} is negative")
            else:
                print(f"{x} is zero")
                print("Operation completed")
        elif choice == "9":
            fruit1, fruit2, fruit3 = "apple", "banana", "orange"
            fruit4 = fruit5 = fruit6 = "lime"
            fruits = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6]
            print(fruits[0])
            print(fruits[1])
            print(fruits[2])
            print(fruits[0] + fruits[1] + fruits[2])
            print(fruits[3] + fruits[4] + fruits[5])
            print("Operation completed")
        elif choice == "10":
            Re = float(input("Enter a real number: "))
            Im = float(input("Enter an imaginary number: "))
            print(f"The complex number is: {Re + Im * 1j}")
            Op = input("Enter an operation (+, -, *, /, Polar, Cartesian): ")
            if Op == "+":
                print(f"The sum is: {Re + Im * 1j + Re + Im * 1j}")
            elif Op == "-":
                print(f"The difference is: {Re + Im * 1j - Re + Im * 1j}")
            elif Op == "*":
                print(f"The product is: {Re + Im * 1j * Re + Im * 1j}")
            elif Op == "/":
                print(f"The quotient is: {Re + Im * 1j / Re + Im * 1j}")
            elif Op == "Polar":
                print(f"The polar representation is: {abs(Re + Im * 1j)}")
            elif Op == "Cartesian":
                print(f"The Cartesian representation is: {Re + Im * 1j}")
            else:
                print("Invalid operation")
            plot = input("Would you like to plot? (yes/no): ")
            if plot == "yes":
                type = input("What type of plot? Polar, Cartesian, or Both? (p,c,b): ")
                if type == "p":
                    print(f"Polar plot of {Re + Im * 1j}")
                    r = np.arange(0, 2 * np.pi, 0.01)
                    theta = 2 * np.pi * r
                    plt.polar(r, theta)
                    plt.show()
                elif type == "c":
                    print(f"Cartesian plot of {Re + Im * 1j}")
                    x = np.linspace(-10, 10, 100)
                    y = np.linspace(-10, 10, 100)
                    X, Y = np.meshgrid(x, y)
                    Z = X + Y * 1j
                    plt.contourf(X, Y, np.abs(Z - (Re + Im * 1j)), cmap="viridis")
                    plt.colorbar()
                    plt.show()
                elif type == "b":
                    print(f"Both plots of {Re + Im * 1j}")
                else:
                    print("Invalid plot type")
            elif plot == "no":
                print("Not plotting.")
                print("Operation completed")
            else:
                print("Invalid response.")

        elif choice == "11":
            bit0 = bool(input("Enter bit value: (0 or 1): "))
            bit1 = bool(input("Enter bit value: (0 or 1): "))
            Op = input(
                "Enter operation: (and, or, xor, left shift, right shift, left rotate, right rotate, bitwise and, bitwise or, bitwise xor): "
            )
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
                print("Operation completed")
        elif choice == "12":
            print("Exiting...")
            complete = 1
        else:
            print("Invalid choice")


"""
        a = True
        b = True

        sum, c = half_adder(a, b)
        result, carry = full_adder(sum, c, False)
        print("Result:", result)

        for i in range(1, 10):
            print("random number:", rnd.randrange(1, 10))

        digit = rnd.randrange(1, 15)
        pi = math.pi
        pi_array = str(pi).split(".")[1]
        print("The", digit + 1, "digit of pi is", pi_array[digit])
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
        print("Pi hard:", pi_digits[digit])

        print("Is equal:", pi_array[digit] is not pi_digits[digit])

        # Check if a number is prime
        is_prime = True
        for i in range(2, int(math.sqrt(pi_digits[digit])) + 1):
            if pi_digits[digit] % i == 0:
                is_prime = False
                break

        print("Is prime:", is_prime)

        # Check if a number is even
        is_even = pi_digits[digit] % 2 == 0
        print("Is even:", is_even)

        # Check if a number is odd
        is_odd = pi_digits[digit] % 2 != 0
        print("Is odd:", is_odd)

        # Check if a number is divisible by n
        n = 3
        is_divisible_by_n = pi_digits[digit] % n == 0
        print("Is divisible by", n, ":", is_divisible_by_n)

        # List - ordered and changeable, duplicates allowed
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print("List:", my_list)

        # Add an element to the list
        my_list.append(11)
        print("List after appending:", my_list)

        # Remove an element from the list
        my_list.remove(5)
        print("List after removing:", my_list)

        # Sort the list
        my_list.sort()
        print("List after sorting:", my_list)

        # Reverse the list
        my_list.reverse()
        print("List after reversing:", my_list)

        # Insert an element at a specific index
        my_list.insert(2, 12)
        print("List after inserting:", my_list)

        # Remove an element at a specific index
        my_list.pop(2)
        print("List after popping:", my_list)

        # Tuple - ordered and unchangeable, duplicates allowed
        my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        print("Tuple:", my_tuple)

        # Set - unordered and unchangeable, no duplicates allowed
        my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        print("Set:", my_set)

        # Dictionary - unordered and changeable, no duplicates allowed
        my_dict = {"name": "John", "age": 30, "city": "New York"}
        print("Dictionary:", my_dict)

        # Set - unordered and unchangeable, no duplicates allowed
        my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        print("Set:", my_set)

        # Dictionary - unordered and changeable, no duplicates allowed
        my_dict = {"name": "John", "age": 30, "city": "New York"}
        print("Dictionary:", my_dict)

        # Pass statement - used to avoid error
        a = True
        b = False
        if a != b:
            pass
        else:
            print("its false")

        print("")

        # Match statement - used to match values
        match my_list:
            case [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                print("List matches")
            case _:
                print("List does not match")

        def my_generator():
            yield 1
            yield 2
            yield 3

        for value in my_generator():
            print(value)

        gen = fibonacci()
        for _ in range(rnd.randint(1, 100)):
            print("random fibonacci number:", next(gen))

        x = range(0, 10, 1)
        y = np.sin(x)
        y = x

        # plot
        plt.plot(x, y)
        plt.show()

        # Degrees to radians
        def degrees_to_radians(degrees):
            return degrees * (math.pi / 180)

        # Radians to degrees
        def radians_to_degrees(radians):
            return radians * (180 / math.pi)

        arr = rnd.randint(1, 100)
        arr_deg = degrees_to_radians(arr)
        arr_rad = radians_to_degrees(arr_deg)

        print("arr_deg:", arr_deg)
        print("arr_rad:", arr_rad)
        print("arr:", arr)

        # complete
        complete = 1

        # Complete the program
        if complete == 1:
            print("Program completed successfully.")
        else:
            print("Program not completed.")
            continue
        break

"""

main()  # Call the main function to start the program.
