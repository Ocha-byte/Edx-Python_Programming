# Written by Charles Underwood
# Menu file

import tkinter as tk
import tkinter.font as tkfont


def button_clicked(menu):
    print(menu, "button clicked!")


def exit_button(root):
    exit_button = tk.Button(
        root,
        text="Exit",
        command=root.destroy,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    print("Exiting App....")

    # Pack the label into the mainframe
    exit_button.pack(padx=20, pady=20)

    return exit_button


def main_menu_button(root):
    main_menu_button = tk.Button(
        root,
        text="Main Menu",
        command=lambda: button_clicked("main menu"),
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    main_menu_button.pack(padx=20, pady=20)

    return main_menu_button


def main_menu(root):
    # Create a label widget
    main_text_var = tk.StringVar()
    main_text_var.set("Main Menu Label")
    main_text_label = tk.Label(
        root,
        textvariable=main_text_var,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    main_text_label.pack(padx=20, pady=20)

    return main_menu


def profile(root):
    # Create a label widget
    profile_text_var = tk.StringVar()
    profile_text_var.set("Profile")
    profile_text_label = tk.Label(
        root,
        textvariable=profile_text_var,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    profile_text_label.pack(padx=20, pady=20)

    return profile_text_label


def practice(root):
    # Create a label widget
    practice_text_var = tk.StringVar()
    practice_text_var.set("Practice")
    practice_text_label = tk.Label(
        root,
        textvariable=practice_text_var,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    practice_text_label.pack(padx=20, pady=20)

    return practice_text_label


def personal_stats(root):
    # Create a label widget
    personal_stats_text_var = tk.StringVar()
    personal_stats_text_var.set("Personal Stats")
    personal_stats_text_label = tk.Label(
        root,
        textvariable=personal_stats_text_var,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    personal_stats_text_label.pack(padx=20, pady=20)

    return personal_stats_text_label


def dictionary(root):
    # Create a label widget
    dictionary_text_var = tk.StringVar()
    dictionary_text_var.set("Dictionary")
    dictionary_text_label = tk.Label(
        root,
        textvariable=dictionary_text_var,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    dictionary_text_label.pack(padx=20, pady=20)

    return dictionary_text_label


def settings(root):
    # Create a label widget
    settings_text_var = tk.StringVar()
    settings_text_var.set("Settings")
    settings_text_label = tk.Label(
        root,
        textvariable=settings_text_var,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    settings_text_label.pack(padx=20, pady=20)

    return settings_text_label


def about(root):
    # Create a label widget
    about_text_var = tk.StringVar()
    about_text_var.set("About")
    about_text_label = tk.Label(
        root,
        textvariable=about_text_var,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    about_text_label.pack(padx=20, pady=20)

    return about_text_label


def help(root):
    # Create a label widget
    help_text_var = tk.StringVar()
    help_text_var.set("Help")
    help_text_label = tk.Label(
        root,
        textvariable=help_text_var,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    help_text_label.pack(padx=20, pady=20)

    return help_text_label


def contact(root):
    # Create a label widget
    contact_text_var = tk.StringVar()
    contact_text_var.set("Contact")
    contact_text_label = tk.Label(
        root,
        textvariable=contact_text_var,
        anchor=tk.CENTER,
        bg="lightblue",
        height=3,
        width=30,
        bd=3,
        font=("Helvetica", 16, "bold"),
        cursor="hand2",
        fg="blue",
        padx=15,
        pady=15,
        justify=tk.CENTER,
        relief=tk.RAISED,
        underline=0,
        wraplength=250,
    )

    # Pack the label into the mainframe
    contact_text_label.pack(padx=20, pady=20)

    return contact_text_label
