# The scroll bar class for the main app file.

import tkinter as tk
import tkinter.font as tkfont


class ScrollBar:
    def __init__(self, root):
        self.root = root
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def configure_scrollbar(self, widget):
        widget.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=widget.yview)

    def pack_scrollbar(self):
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
