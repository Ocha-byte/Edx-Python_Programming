import tkinter as tk
import tkinter.font as tkfont


def increase_font_size():
    font.config(size=font.actual()["size"] + 2)


def decrease_font_size():
    font.config(
        size=max(8, font.actual()["size"] - 2)
    )  # Ensure font size doesn't go below 8


def reset_font_size():
    font.config(family="Helvetica", size=12, weight="normal")


root = tk.Tk()
font = tkfont.Font(family="Helvetica", size=12)
label = tk.Label(root, text="Resizable Text", font=font)
label.pack()

increase_button = tk.Button(root, text="Increase", command=increase_font_size)
increase_button.pack()

decrease_button = tk.Button(root, text="Decrease", command=decrease_font_size)
decrease_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_font_size)
reset_button.pack()

root.mainloop()
