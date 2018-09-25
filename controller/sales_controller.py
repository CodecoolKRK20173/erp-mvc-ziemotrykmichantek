# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
from controller import common

def run():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    options = ['Create',
               'Read',
               'Update',
               'Delete']

    terminal_view.print_menu(options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            sales.add(data_manager.get_table_from_file('model/sales/sales.csv', terminal_view.get_record() ))
        elif choice == "2":
            sales.update(data_manager.get_table_from_file('model/sales/sales.csv', terminal_view.get_id() ))
        elif choice == "3":
            sales.remove(data_manager.get_table_from_file('model/sales/sales.csv', terminal_view.get_id() ))
        else:
            terminal_view.print_error_message("There is no such choice.")
