""" Common functions for controllers
implement commonly used functions here
"""
from view import terminal_view

def common_controller(create_function, read_function, update_function, delete_function, table):
    options = ['Create',
               'Read',
               'Update',
               'Delete']

    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    print('COMMON CONTROLLER SIE ODPALA')
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            create_function(table)
        elif choice == "2":
            read_function(table)
        elif choice == "3":
            update_function(table)
        elif choice == "4":
            delete_function(table)
        else:
            terminal_view.print_error_message("There is no such choice.")

def fun(f, table):
    f(table, 'kH35Jr#&', ['Age of EmpFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFires II', 'The Age of Kings', 32,10,23,2019])
