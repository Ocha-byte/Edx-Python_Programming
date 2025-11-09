# Written by Charles Underwood
# Interpretied: Python hello.py
# The main file with mostly my own code.

import fun_module as fun  # My local module
import programs as prog

import numpy as np
import random as rnd
import math as math
import matplotlib.pyplot as plt
import datetime as dt


def main():
    complete = 0
    while complete != 1:
        prog.main()

        choice = 0  # Pre-allocation

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Hello world!")
        elif choice == "2":
            fun.hello_user()
        elif choice == "3":
            fun.cmonth()
        elif choice == "4":
            fun.plotting()
        elif choice == "5":
            fun.arithmetic_operations()
        elif choice == "6":
            fun.powers()
        elif choice == "7":
            fun.divider()
        elif choice == "8":
            fun.pos_or_neg()
        elif choice == "9":
            fun.fruity_array()
        elif choice == "10":
            fun.complex_numbers()
        elif choice == "11":
            fun.bit_ops()
        elif choice == "12":
            fun.adders()
        elif choice == "13":
            fun.rnd_pi()
        elif choice == "14":
            fun.check_prime()
        elif choice == "15":
            fun.odd_evens()
        elif choice == "16":
            fun.fibonacci()
        elif choice == "17":
            print("Exiting...")
            complete = 1
        else:
            print("Invalid choice")


"""


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
