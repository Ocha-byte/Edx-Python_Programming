# Written by Charles Underwood
# Menu buttons file

import tkinter as tk
import tkinter.font as tkfont

import main_app as ma
import set_menu as sm


def increase_font_size():
    ma.font.config(size=ma.font.actual()["size"] + 2)


def decrease_font_size():
    ma.font.config(
        size=max(8, ma.font.actual()["size"] - 2)
    )  # Ensure font size doesn't go below 8


def reset_font_size():
    ma.font.config(family="Helvetica", size=16, weight="bold")


def font_properties(action):
    if action == "increase":
        increase_font_size()
    elif action == "decrease":
        decrease_font_size()
    elif action == "reset":
        reset_font_size()
    elif action == "default":
        return tkfont.Font(family="Helvetica", size=16, weight="bold")
    elif action == "current":
        return ma.font


class MenuButtons:
    def __init__(self, root):
        self.root = root
        self.buttons = []

    # Create buttons using grid
    def create_button(self, text, command):
        button = tk.Button(
            self.root,
            text=text,
            command=command,
            bg="lightblue",
            height=1,
            width=15,
            bd=1,
            font=ma.font,
            # font=tkfont.Font(family="Helvetica", size=16, weight="bold"),
            cursor="hand2",
            fg="blue",
            underline=0,
            wraplength=250,
        )

        # Pack the label into the mainframe
        button.grid(padx=20, pady=20)

        return button


def exit_button(root):
    exit_button = MenuButtons(root).create_button("Exit", root.destroy)
    return exit_button


def main_menu_button(root):
    main_menu_button = MenuButtons(root).create_button(
        "Main Menu",
        lambda: sm.current_display(root, "main_menu"),
    )
    return main_menu_button


def profile_button(root):
    profile_button = MenuButtons(root).create_button(
        "Profile",
        lambda: sm.current_display(root, "profile"),
    )
    return profile_button


def practice_button(root):
    practice_button = MenuButtons(root).create_button(
        "Practice",
        lambda: sm.current_display(root, "practice"),
    )
    return practice_button


def personal_stats_button(root):
    personal_stats_button = MenuButtons(root).create_button(
        "Personal Stats", lambda: sm.current_display(root, "personal_stats")
    )
    return personal_stats_button


def dictionary_button(root):
    dictionary_button = MenuButtons(root).create_button(
        "Dictionary", lambda: sm.current_display(root, "dictionary")
    )
    return dictionary_button


def settings_button(root):
    settings_button = MenuButtons(root).create_button(
        "Settings", lambda: sm.current_display(root, "settings")
    )
    return settings_button


def about_button(root):
    about_button = MenuButtons(root).create_button(
        "About", lambda: sm.current_display(root, "about")
    )
    return about_button


def help_button(root):
    help_button = MenuButtons(root).create_button(
        "Help", lambda: sm.current_display(root, "help")
    )
    return help_button


def contact_button(root):
    contact_button = MenuButtons(root).create_button(
        "Contact", lambda: sm.current_display(root, "contact")
    )
    return contact_button


def feedback_button(root):
    feedback_button = MenuButtons(root).create_button(
        "Feedback", lambda: sm.current_display(root, "feedback")
    )
    return feedback_button
