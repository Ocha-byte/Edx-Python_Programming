# Written by Charles Underwood
# Keeps track of the user selection.


import fun_module as fun


def user_choice():
    choice = input("Enter your choice: ")
    return choice


def main():
    choice = user_choice()

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
        fun.scramble()
    elif choice == "18":
        fun.encrypt()
    elif choice == "19":
        fun.encrypted_scramble()
    elif choice == "20":
        fun.decrypted_scramble()
    elif choice == "21":
        fun.decrypt()
    elif choice == "22":
        fun.unscramble()
    elif choice == "23":
        fun.deg_or_rads()
    elif choice == "24":
        print("Exiting...")
    else:
        print("Invalid choice")
