# Written by Charles Underwood
# To run: Python main.py
# The main app file.

import tkinter as tk
import tkinter.font as tkfont

import main_menu as mm
import menus.about_menu as am
import menus.contact_menu as cm
import menus.dictionary_menu as dm
import menus.help_menu as hm
import menus.personal_stats_menu as psm
import menus.practice_menu as pracm
import menus.profile_menu as pfm
import menus.settings_menu as sm

# Initialize the root window
root = tk.Tk()

# Set the window title
root.title("German Learning App")
root.geometry("800x600")

# Initialize the main frame
main_frame = tk.Frame(root)

# Create a frame for the buttons
button_frame = tk.Frame(main_frame)

# Make the grid cell expandable
button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_columnconfigure(0, weight=1)

mm.display_main_menu(root)

# Resize the window to fit the content
root.resizable(True, True)

# Root window main loop
root.mainloop()


def main():
    print("")
