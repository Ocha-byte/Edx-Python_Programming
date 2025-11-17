import tkinter as tk

import menu_buttons as mb


def clear_display(root):
    for widget in root.winfo_children():
        widget.destroy()


def current_display(root, menu):
    clear_display(root)
    if menu == "main_menu":
        return display_main_menu(root)
    elif menu == "profile":
        return display_profile_page(root)
    elif menu == "practice":
        return display_practice_page(root)
    elif menu == "personal_stats":
        return display_personal_stats_page(root)
    elif menu == "dictionary":
        return display_dictionary_page(root)
    elif menu == "settings":
        return display_settings_page(root)
    elif menu == "about":
        return display_about_page(root)
    elif menu == "help":
        return display_help_page(root)
    elif menu == "contact":
        return display_contact_page(root)
    elif menu == "feedback":
        return display_feedback_page(root)
    elif menu == "default":
        return display_main_menu(root)
    else:
        raise ValueError(f"Invalid menu: {menu}")


def display_main_menu(root):
    # Create label
    label = tk.Label(root, text="Main Menu")
    label.grid(row=0, column=0, columnspan=3)

    # Button positions in the grid
    mb.main_menu_button(root).grid(row=1, column=0)
    mb.profile_button(root).grid(row=1, column=1)
    mb.practice_button(root).grid(row=1, column=2)

    mb.personal_stats_button(root).grid(row=2, column=0)
    mb.dictionary_button(root).grid(row=2, column=1)
    mb.settings_button(root).grid(row=2, column=2)

    mb.about_button(root).grid(row=3, column=0)
    mb.help_button(root).grid(row=3, column=1)
    mb.contact_button(root).grid(row=3, column=2)

    mb.feedback_button(root).grid(row=4, column=0)
    mb.exit_button(root).grid(row=4, column=1)

    return display_main_menu


def display_profile_page(root):
    # Create label
    label = tk.Label(root, text="Profile Page")
    label.grid(row=0, column=0, columnspan=3)

    # Button positions in the grid
    mb.main_menu_button(root).grid(row=1, column=0)

    mb.exit_button(root).grid(row=3, column=1)

    return display_profile_page


def display_practice_page(root):
    # Create label
    label = tk.Label(root, text="Practice Page")
    label.grid(row=0, column=0, columnspan=3)

    # Button positions in the grid
    mb.main_menu_button(root).grid(row=1, column=0)

    mb.exit_button(root).grid(row=3, column=1)

    return display_practice_page


def display_personal_stats_page(root):
    # Create label
    label = tk.Label(root, text="Personal Stats Page")
    label.grid(row=0, column=0, columnspan=3)

    # Button positions in the grid
    mb.main_menu_button(root).grid(row=1, column=0)

    mb.exit_button(root).grid(row=3, column=1)

    return display_personal_stats_page


def display_dictionary_page(root):
    # Create label
    label = tk.Label(root, text="Dictionary Page")
    label.grid(row=0, column=0, columnspan=3)

    # Button positions in the grid
    mb.main_menu_button(root).grid(row=1, column=0)

    mb.exit_button(root).grid(row=3, column=1)

    return display_dictionary_page


def display_settings_page(root):
    # Create label
    label = tk.Label(root, text="Settings Page")
    label.grid(row=0, column=0, columnspan=3)

    mb.main_menu_button(root).grid(row=1, column=0)

    # Font size
    increase_button = tk.Button(root, text="Increase", command=mb.increase_font_size)
    increase_button.grid(row=2, column=0)

    decrease_button = tk.Button(root, text="Decrease", command=mb.decrease_font_size)
    decrease_button.grid(row=2, column=1)

    reset_button = tk.Button(root, text="Reset", command=mb.reset_font_size)
    reset_button.grid(row=2, column=2)

    mb.exit_button(root).grid(row=3, column=1)

    return display_settings_page


def display_about_page(root):
    # Create label
    label = tk.Label(root, text="About Page")
    label.grid(row=0, column=0, columnspan=3)

    # Button positions in the grid
    mb.main_menu_button(root).grid(row=1, column=0)

    mb.exit_button(root).grid(row=3, column=1)

    return display_about_page


def display_help_page(root):
    # Create label
    label = tk.Label(root, text="Help Page")
    label.grid(row=0, column=0, columnspan=3)

    # Button positions in the grid
    mb.main_menu_button(root).grid(row=1, column=0)

    mb.exit_button(root).grid(row=3, column=1)

    return display_help_page


def display_contact_page(root):
    # Create label
    label = tk.Label(root, text="Contact Page")
    label.grid(row=0, column=0, columnspan=3)

    # Button positions in the grid
    mb.main_menu_button(root).grid(row=1, column=0)

    mb.exit_button(root).grid(row=3, column=1)

    return display_contact_page


def display_feedback_page(root):
    # Create label
    label = tk.Label(root, text="Feedback Page")
    label.grid(row=0, column=0, columnspan=3)

    # Button positions in the grid
    mb.main_menu_button(root).grid(row=1, column=0)

    mb.exit_button(root).grid(row=3, column=1)

    return display_feedback_page
