""" Common functions for controllers
implement commonly used functions here
"""
from view import terminal_view
from model import data_manager
import os

def clear_function():
    os.system('clear')

def common_controlls(options, title_list, file_name, controll_name):
    table = data_manager.get_table_from_file(file_name)
    terminal_view.print_primitive_logo()
    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice()
        table = data_manager.get_table_from_file(file_name)
        clear_function()
        if choice == "1":
            data_manager.write_table_to_file(file_name ,controll_name.add(table, terminal_view.get_record() ))
            terminal_view.print_primitive_logo()
            table = data_manager.get_table_from_file('model/accounting/items.csv')
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "2":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "3":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            data_manager.write_table_to_file(file_name ,controll_name.update(table, terminal_view.get_id() ))
            table = data_manager.get_table_from_file('model/accounting/items.csv')
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "4":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            data_manager.write_table_to_file(file_name ,controll_name.remove(table, terminal_view.get_id() ))
            table = data_manager.get_table_from_file('model/accounting/items.csv')
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "5":
            terminal_view.print_primitive_logo()
            terminal_view.print_result(controll_name.which_year_max(table))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "6":
            year = terminal_view.get_year()
            terminal_view.print_primitive_logo()
            terminal_view.print_result(accounting.avg_amount(table, year))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        else:
            terminal_view.print_primitive_logo()
            terminal_view.print_error_message("There is no such choice.")
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
