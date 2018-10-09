# everything you'll need is imported:
from model.store import store
from view import terminal_view
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
               'Check how many different kinds of games in data',
               'Check avarage amount of games in stock of given manufacturer in data']

    get_record_data = (['Title: ', 'Manufacturer: ', 'Price: ', 'In stock: '], 'New Record:')
    title_list = ["id", "title", "manufacturer", "price", "in_stock"]
    table = data_manager.get_table_from_file('model/store/games.csv')
    file_name = 'model/store/games.csv'

    terminal_view.print_primitive_logo()
    terminal_view.print_menu("Choose option:", options, "Back to main menu")
    choice = None
    while choice != "0":
        choice = terminal_view.get_choice()
        table = data_manager.get_table_from_file(file_name)
        common.clear_function()
        if choice == "1":
            data_manager.write_table_to_file(file_name ,store.add(table, terminal_view.get_record(get_record_data) ))
            table = data_manager.get_table_from_file('model/accounting/items.csv')
            terminal_view.print_primitive_logo()
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "2":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "3":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            data_manager.write_table_to_file(file_name ,store.update(table, terminal_view.get_id() ))
            table = data_manager.get_table_from_file('model/accounting/items.csv')
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "4":
            terminal_view.print_primitive_logo()
            terminal_view.print_table(table, title_list)
            data_manager.write_table_to_file(file_name ,store.remove(table, terminal_view.get_id() ))
            table = data_manager.get_table_from_file('model/accounting/items.csv')
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "5":
            terminal_view.print_primitive_logo()
            terminal_view.print_result(store.get_counts_by_manufacturers(table))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        elif choice == "6":
            manufacturer = terminal_view.get_manufacturer
            terminal_view.print_primitive_logo()
            terminal_view.print_result(store.get_average_by_manufacturer(table, manufacturer))
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
        else:
            terminal_view.print_primitive_logo()
            terminal_view.print_error_message("There is no such choice.")
            terminal_view.print_menu("Choose option:",options,"Back to main menu")
