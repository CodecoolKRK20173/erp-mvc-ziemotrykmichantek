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
               'Delete',
               'Show the id of the customer with the longest name',
               'Show which customer has subcribed to the newsletter']

    title_list = ["id", "name", "email", "subscribed"]
    table = data_manager.get_table_from_file('model/crm/customers.csv')

    terminal_view.print_primitive_logo()
    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice()
        common.clear_function()
        if choice == "1":
            crm.add(table, terminal_view.get_record() )
            terminal_view.print_primitive_logo()
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            terminal_view.print_primitive_logo()
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "3":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            crm.update(table, terminal_view.get_id() )
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "4":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            crm.remove(table, terminal_view.get_id() )
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "5":
            crm.get_longest_name_id(table)
            terminal_view.print_primitive_logo()
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "6":
            crm.get_subscribed_emails(table)
            terminal_view.print_primitive_logo()
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        else:
            terminal_view.print_primitive_logo()
            terminal_view.print_error_message("There is no such choice.")
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
