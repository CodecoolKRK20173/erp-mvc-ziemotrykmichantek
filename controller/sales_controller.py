# everything you'll need is imported:
from view import terminal_view
from model.sales import sales
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
               'Show lowest prize item id',
               'Show items sold between given dates']

    title_list = ["id", "title", "price", "month", "day", "year"]
    table = data_manager.get_table_from_file('model/sales/sales.csv')

    terminal_view.print_menu("Choose option:",options,"Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice()
        common.clear_function()
        if choice == "1":
            sales.add(table, terminal_view.get_record() )
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "2":
            terminal_view.print_table(table, title_list)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "3":
            sales.update(table, terminal_view.get_id() )
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "4":
            sales.remove(table, terminal_view.get_id() )
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "5":
            sales.get_lowest_price_item_id(table)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "6":
            sales.get_items_sold_between(table)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
            inputs = get_from_to_date()
            month_from, day_from, year_from, month_to, day_to, year_to = inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5]
            get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
        else:
            terminal_view.print_error_message("There is no such choice.")
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
