import tkinter as tk

import menu_buttons as mb


def display_main_menu(root):
    # Button positions in the grid
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

    return display_main_menu
