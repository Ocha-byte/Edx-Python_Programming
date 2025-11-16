import datetime as dt
import tkinter as tk

from pytz import timezone


class digital_clock:
    def __init__(self, root, tz):
        self.root = root
        self.tz = timezone(tz)
        self.label = tk.Label(root, font=("Helvetica", 24), bg="white", fg="black")
        self.label.pack()
        self.update_time()

    def update_time(self):
        current_time = dt.datetime.now(self.tz)
        location = self.tz
        time_str = current_time.strftime("%H:%M:%S")
        self.label.config(text=f"{location}: {time_str}")
        self.root.after(1000, self.update_time)

    def draw_digital_clock(self):
        self.label.pack()
        self.update_time()
