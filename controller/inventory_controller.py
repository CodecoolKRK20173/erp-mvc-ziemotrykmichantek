# everything you'll need is imported:
from view import terminal_view
from model.inventory import inventory
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
               'Show which items have not exceeded their durability',
               'Show avarage durability time for each manufacturer']

    title_list = ["id", "name", "manufacturer", "purchase_year", "durability"]
    table = data_manager.get_table_from_file('model/inventory/inventory.csv')

    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice()
        common.clear_function()
        if choice == "1":
            inventory.add(table, terminal_view.get_record() ))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "3":
            inventory.update(table, terminal_view.get_id() ))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "4":
            inventory.remove(table, terminal_view.get_id() ))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "5":
            inventory.get_available_items(table))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "6":
            inventory.get_average_durability_by_manufacturers(table))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        else:
            terminal_view.print_error_message("There is no such choice.")
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
