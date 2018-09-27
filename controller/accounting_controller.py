# everything you'll need is imported:
from view import terminal_view
from model.accounting import accounting
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
               'Show which year has the highest profit',
               'Show the avarage profit in given year for every transaction']

    title_list = ["id", "month", "day", "year", "type", "amount"]
    table = data_manager.get_table_from_file('model/accounting/items.csv')

    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice()
        common.clear_function()
        if choice == "1":
            accounting.add(table, terminal_view.get_record() )
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "3":
            accounting.update(table, terminal_view.get_id() )
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "4":
            accounting.remove(table, terminal_view.get_id() )
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "5":
            accounting.which_year_max(table)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "6":
            accounting.avg_amount(table, year) # input needed
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        else:
            terminal_view.print_error_message("There is no such choice.")
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
