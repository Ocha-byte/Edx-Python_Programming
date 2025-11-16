import tkinter as tk

import draw_clock as dc

# Create a Tkinter window
root = tk.Tk()
root.title("Australia-Switzerland Clock")

# Timezones
tz_au = "Australia/Brisbane"
tz_ch = "Europe/Zurich"

# Start drawing the clock
au_clock = dc.digital_clock(root, tz_au)
ch_clock = dc.digital_clock(root, tz_ch)

# Run the Tkinter event loop
root.mainloop()
