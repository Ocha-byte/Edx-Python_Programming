import tkinter as tk

import draw_clock as dc

# Create a Tkinter window
root = tk.Tk()
root.title("Simple Digital Clock")

# Timezones
tz_au = "Australia/Brisbane"
tz_ch = "Europe/Zurich"
tz_ca = "America/Vancouver"

# Start drawing the clock
au_clock = dc.digital_clock(root, tz_au)
ch_clock = dc.digital_clock(root, tz_ch)
ca_clock = dc.digital_clock(root, tz_ca)

# Run the Tkinter event loop
root.mainloop()
