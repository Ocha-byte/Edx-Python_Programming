# Written by Charles Underwood
# Menu buttons file

import tkinter as tk
import tkinter.font as tkfont


def button_clicked(menu):
    print(menu, "button clicked!")


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
            font=("Helvetica", 16, "bold"),
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
        "Main Menu", lambda: button_clicked("main menu")
    )
    return main_menu_button


def profile_button(root):
    profile_button = MenuButtons(root).create_button(
        "Profile", lambda: button_clicked("profile")
    )
    return profile_button


def practice_button(root):
    practice_button = MenuButtons(root).create_button(
        "Practice", lambda: button_clicked("practice")
    )
    return practice_button

    return practice_button


def personal_stats_button(root):
    personal_stats_button = MenuButtons(root).create_button(
        "Personal Stats", lambda: button_clicked("personal_stats")
    )
    return personal_stats_button


def dictionary_button(root):
    dictionary_button = MenuButtons(root).create_button(
        "Dictionary", lambda: button_clicked("dictionary")
    )
    return dictionary_button


def settings_button(root):
    settings_button = MenuButtons(root).create_button(
        "Settings", lambda: button_clicked("settings")
    )
    return settings_button


def about_button(root):
    about_button = MenuButtons(root).create_button(
        "About", lambda: button_clicked("about")
    )
    return about_button


def help_button(root):
    help_button = MenuButtons(root).create_button(
        "Help", lambda: button_clicked("help")
    )
    return help_button


def contact_button(root):
    contact_button = MenuButtons(root).create_button(
        "Contact", lambda: button_clicked("contact")
    )
    return contact_button
