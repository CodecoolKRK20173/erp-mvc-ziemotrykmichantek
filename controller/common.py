""" Common functions for controllers
implement commonly used functions here
"""
from view import terminal_view

def common_controller(create_function, read_function, update_function, delete_function):
    options = ['Create',
               'Read',
               'Update',
               'Delete']

    terminal_view.print_menu(options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            create_function
        elif choice == "2":
            read_function
        elif choice == "3":
            update_function
        elif choice == "4":
            delete_function
        else:
            terminal_view.print_error_message("There is no such choice.")
