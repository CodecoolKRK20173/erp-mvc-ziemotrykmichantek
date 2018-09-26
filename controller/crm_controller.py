# everything you'll need is imported:
from view import terminal_view
from model.crm import crm
from controller import common
from model import data_manager

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

    title_list = ["id", "name", "email", "subscribed"]

    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice(options)
        if choice == "1":
            crm.add(data_manager.get_table_from_file('mode/crm/customers.csv', terminal_view.get_record() ))
        elif choice == "2":
            crm.update(data_manager.get_table_from_file('mode/crm/customers.csv', terminal_view.get_id() ))
        elif choice == "3":
            crm.remove(data_manager.get_table_from_file('mode/crm/customers.csv', terminal_view.get_id() ))
        else:
            terminal_view.print_error_message("There is no such choice.")
