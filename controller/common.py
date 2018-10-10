""" Common functions for controllers
implement commonly used functions here
"""
from view import terminal_view
from model import data_manager
import os

def clear_function():
    os.system('clear')

def common_controlls(options, title_list, file_name, controll_name, get_record_data, crm_or_extended_sales=None):
    table = data_manager.get_table_from_file(file_name)
    terminal_view.print_primitive_logo()
    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice()
        table = data_manager.get_table_from_file(file_name)
        clear_function()
        if choice == "1":
            data_manager.write_table_to_file(file_name ,controll_name.add(table, terminal_view.get_record(get_record_data) ))
            terminal_view.print_primitive_logo()
            table = data_manager.get_table_from_file(file_name)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "2":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "3":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            data_manager.write_table_to_file(file_name ,controll_name.update(table, terminal_view.get_id() ))
            table = data_manager.get_table_from_file(file_name)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "4":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            data_manager.write_table_to_file(file_name ,controll_name.remove(table, terminal_view.get_id() ))
            table = data_manager.get_table_from_file(file_name)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "5":
            terminal_view.print_primitive_logo()
            terminal_view.print_result(controll_name.special_function(table))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "6":
            terminal_view.print_primitive_logo()
            terminal_view.print_result(controll_name.special_function2(table))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        else:
            if crm_or_extended_sales:
                pass
            elif not crm_or_extended_sales:
                pass
            else:
                terminal_view.print_primitive_logo()
                terminal_view.print_error_message("There is no such choice.")
                terminal_view.print_menu("Choose option:",options,"Back to main menu")

def extended_sales(choice):
    table = data_manager.get_table_from_file('data_analyser/buyers.csv')
    if choice == "7":
        pass
    elif choice == "8":
        pass
    elif choice == "9":
        pass
    elif choice == "10":
        pass
    elif choice == "11":
        pass
    elif choice == "12":
        pass
    elif choice == "13":
        pass

def extended_crm(choice, table):
    if choice == "7":
        pass
