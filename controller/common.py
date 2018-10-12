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
        choice = terminal_view.get_choice().upper()
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
            data_manager.write_table_to_file(file_name ,controll_name.update(table, terminal_view.get_id(), terminal_view.get_record(get_record_data) ))
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
                extended_sales(choice, controll_name)
                terminal_view.print_menu("Choose option:",options,"Back to main menu")
            elif not crm_or_extended_sales:
                extended_crm(choice, table, controll_name, title_list)
                terminal_view.print_menu("Choose option:",options,"Back to main menu")
            else:
                terminal_view.print_primitive_logo()
                terminal_view.print_error_message("There is no such choice.")
                terminal_view.print_menu("Choose option:",options,"Back to main menu")

def extended_sales(choice, controll_name):
    table = data_manager.get_table_from_file('data_analyser/buyers.csv')
    title_list = ["buyer id", "name","title", "price", "month", "day", "year", "sale id"]
    if choice == "7":
        terminal_view.print_primitive_logo()
        terminal_view.print_table(table, title_list)
        terminal_view.print_result(controll_name.get_title_by_id_from_table(table, terminal_view.get_id()))
    elif choice == "8":
        terminal_view.print_primitive_logo()
        terminal_view.print_result(controll_name.get_item_id_or_title_sold_last_from_table(table, False))
    elif choice == "9":
        terminal_view.print_primitive_logo()
        terminal_view.print_result(controll_name.get_the_sum_of_prices_from_table(table))
    elif choice == "A":
        terminal_view.print_primitive_logo()
        terminal_view.print_table(table, title_list)
        terminal_view.print_result(controll_name.get_customer_id_by_sale_id_from_table(table, terminal_view.get_id()))
    elif choice == "B":
        terminal_view.print_primitive_logo()
        terminal_view.print_result(controll_name.get_all_customer_ids_from_table(table))
    elif choice == "C":
        terminal_view.print_primitive_logo()
        terminal_view.print_result(controll_name.get_all_sales_ids_for_customer_ids_from_table(table))
    elif choice == "D":
        terminal_view.print_primitive_logo()
        terminal_view.print_table(table, title_list)
        terminal_view.print_result(controll_name.get_num_of_sales_per_customer_ids_from_table(table, terminal_view.get_id()))

def extended_crm(choice, table, controll_name, title_list):
    if choice == "7":
        terminal_view.print_table(table, title_list)
        terminal_view.print_result(controll_name.get_name_by_id_from_table(table, terminal_view.get_id()))
