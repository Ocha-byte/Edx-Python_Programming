# Written by Charles Underwood
# To run: Python main.py
# The main app file.

import tkinter as tk
import tkinter.font as tkfont

import menu_buttons as mb

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

# Pack the buttons into the button frame
mb.main_menu_button(root).grid(row=0, column=0)
mb.profile_button(root).grid(row=0, column=1)
mb.practice_button(root).grid(row=0, column=2)

mb.personal_stats_button(root).grid(row=1, column=0)
mb.dictionary_button(root).grid(row=1, column=1)
mb.settings_button(root).grid(row=1, column=2)

mb.about_button(root).grid(row=2, column=0)
mb.help_button(root).grid(row=2, column=1)
mb.contact_button(root).grid(row=2, column=2)

mb.exit_button(root).grid(row=3, column=1)

# Resize the window to fit the content
root.resizable(True, True)

# Root window main loop
root.mainloop()


def main():
    print("")
