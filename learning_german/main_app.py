# Written by Charles Underwood
# To run: Python main.py
# The main app file.
import tkinter as tk
import tkinter.font as tkfont

import set_menu

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

# Resize the window to fit the content
root.resizable(True, True)

# Set the font
font = tkfont.Font(family="Helvetica", size=16, weight="bold")

set_menu.current_display(root, "main_menu")

# Root window main loop
root.mainloop()
