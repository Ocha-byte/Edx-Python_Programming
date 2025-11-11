# Written by Charles Underwood
# To run: Python main.py
# The main file.

import tkinter as tk
import tkinter.font as tkfont

import menus as m

# Initialize the root window
root = tk.Tk()

# Set the window title
root.title("German Learning App")
root.geometry("1920x1080")


# Initialize the main frame
main_frame = tk.Frame(root)
main_frame.pack()

m.main_menu_button(root)
m.exit_button(root)

m.main_menu(root)
m.profile(root)
m.practice(root)
m.personal_stats(root)
m.dictionary(root)
m.settings(root)
m.about(root)
m.help(root)
m.contact(root)


# Root window main loop
root.mainloop()


def main():
    print("")
