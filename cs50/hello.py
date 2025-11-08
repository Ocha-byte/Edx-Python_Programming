#
# Course: CS50's Introduction to Programming with Python
# Comppletion Time: 1.783 hrs, 31 October 2025.
# Interpretied: Python hello.py
# This contains code from the course and my own.
#

import fun_module as fun

# import numpy as np
import random as rnd
import math as math
# import matplotlib.pyplot as plt


def main():
    # variables
    # x = 10
    # y = 2 * np.cos(x)
    #
    complete = 0
    while complete != 1:
        # get user input
        name = input("What's your name? ").strip().title()
        print hello user input.
        print(f"Hello {name}!")
        print("Hello world!", end=" ")
        currentMonth = 11
        Month = (float)12
        print(type(Month))
        print("There are", Month, "months in a year")
        print('The current month is', currentMonth)
        print(f"(x,y) = ({x}, {y})")

        # x = float(input("Enter a number: "))
        # y = float(input("Enter another number: "))
        # z_add = round(x + y)
        # z_prod = round(x * y)
        # z_div = round(x / y)
        # z_sub = round(x - y)

        # print(f"The sum of {x} and {y} is {z_add:,.2f}")
        # print(f"The product of {x} and {y} is {z_prod:,.2f}")
        # print(f"The difference of {x} and {y} is {z_sub:,.2f}")
        # print(f"The quotient of {x} and {y} is {z_div:,.2f}")
        # print(f"The remainder of {x} and {y} is {x % y:.2f}")
        # print(f"The power of {x} and {y} is {x**y:.2f}")

        # print(f"The square root of {x} is {sqrt(x):.2f}")
        # print(f"{x}^2 = {square(x):.2f}")

        # print(f"{x}^3 = {nth_power(x, 3):.2f}")
        # print(f"The cube root of {x} is {nth_root(x, 3):.2f}")

        # for i in range(1, 11):
        #    if i % 2 == 0:
        #        print(f"{i} is even")
        #    else:
        #        print(f"{i} is odd")
        # print("Done")

        # fruit1, fruit2, fruit3 = "apple", "banana", "orange"
        # fruit4 = fruit5 = fruit6 = "lime"
        # fruits = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6]

        # print(fruits[0])
        # print(fruits[1])
        # print(fruits[2])
        # print(fruits[0] + fruits[1] + fruits[2])
        # print(fruits[3] + fruits[4] + fruits[5])

        # imagine = 1 + 2j
        # print(imagine)

        # r = range(10)
        # print(list(r))

        # a = True
        # b = False
        # c = a and b  # AND gate
        # d = a or b  # OR gate
        # e = not a
        # f = a ^ b  # XOR gate
        # g = a & b  # Bitwise AND
        # h = a | b  # Bitwise OR
        # i = a ^ b  # Bitwise XOR
        # j = a << 2  # Left shift
        # k = a >> 1  # Right shift

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


main()  # Call the main function to start the program.
