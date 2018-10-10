# everything you'll need is imported:
from model.store import store
from view import terminal_view
from controller import common
from model import data_manager
from data_analyser import data_analyser
import os

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    # your code
    options = ["View the last buyer name",
               "View the last buyer ID",
               "View customer name and money spent",
               "View customer ID and money spent",
               "View the most frequent buyer name",
               "View the most frequent buyer ID"]

    title_list = ["id", "customer", "Tittle", "price", "month", "day", "year"]
    file_name = 'data_analyser/buyers.csv'

    table = data_manager.get_table_from_file(file_name)
    terminal_view.print_primitive_logo()
    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        table = data_manager.get_table_from_file(file_name)
        choice = terminal_view.get_choice()
        os.system('clear')
        terminal_view.print_primitive_logo()
        if choice == "1":
            terminal_view.print_result(data_analyser.get_the_last_buyer_name_or_id(table, True))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "2":
            terminal_view.print_result(data_analyser.get_the_last_buyer_name_or_id(table, False))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "3":
            terminal_view.print_result(data_analyser.get_customer_money_spent_id_or_name(table, True))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "4":
            terminal_view.print_result(data_analyser.get_customer_money_spent_id_or_name(table, False))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "5":
            terminal_view.print_result(data_analyser.get_the_most_frequent_buyers_id_or_name(table, True))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "6":
            terminal_view.print_result(data_analyser.get_the_most_frequent_buyers_id_or_name(table, False))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
